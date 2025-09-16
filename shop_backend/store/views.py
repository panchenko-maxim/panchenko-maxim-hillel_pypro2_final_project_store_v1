from django.contrib.auth import get_user_model
from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status, generics, filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .filters import ProductFilter
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, RegisterSerializer, CartItemSerializer, UserSerializer

User = get_user_model()

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated] 

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['category__name']
    ordering = ['name']
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all() 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 
        
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        
class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        
        if serializer.is_valid():
            user = serializer.save()
        
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)
            refresh_token = str(refresh)
                        
            return Response({
                'message': 'User registered and logged in successfully',
                'access_token': access,
                'refresh_token': refresh_token 
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class CartView(APIView):
    permission_classes = [AllowAny]
    
    def get_cart_key(self, request):
        if request.user.is_authenticated:
            return f"cart:{request.user.id}"
        if not request.session.session_key:
            request.session.save()
        return f"cart:{request.session.session_key}"
    
    def get(self, request):
        cart_key = self.get_cart_key(request)
        cart_data = cache.get(cart_key, [])
        serializer = CartItemSerializer(cart_data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        cart_key = self.get_cart_key(request)
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
        cart_items = cache.get(cart_key, [])
        existing_item = next((item for item in cart_items if item['product_id'] == product_id), None)
        
        user_id = request.user.id if request.user.is_authenticated else None
        
        if existing_item:
            existing_item['quantity'] += quantity
        else:
            cart_items.append({'product_id': product_id, 'quantity': quantity, 'user_id': user_id})
                              
        cache.set(cart_key, cart_items, timeout=60 * 60 * 24 * 7)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        cart_key = self.get_cart_key(request)
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        
        if not all([product_id, quantity is not None]):
            return Response({'error': "product_id and quantity ate required"}, status=status.HTTP_400_BAD_REQUEST)
        
        cart_items = cache.get(cart_key, [])
        item_found = False
        user_id = request.user.id if request.user.is_authenticated else None
        
        for item in cart_items:
            if item['product_id'] == product_id:
                item['quantity'] = quantity
                item['user_id'] = user_id
                item_found = True
                break
        if not item_found:
            return Response({'error': 'Product not in cart'}, status=status.HTTP_404_NOT_FOUND)
        
        cart_items = [item for item in cart_items if item['quantity'] > 0]
        
        cache.set(cart_key, cart_items, timeout=60 * 60 * 24 * 7)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, product_id=None):
        cart_key = self.get_cart_key(request)
        cart_items = cache.get(cart_key, [])
        
        if product_id:
            cart_items = [item for item in cart_items if item['product_id'] != product_id]
        else:
            cart_items = []
            
        cache.set(cart_key, cart_items, timeout=60 * 60 * 24 * 7)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        
    
        


