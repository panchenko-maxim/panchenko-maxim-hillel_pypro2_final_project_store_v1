from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets,status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, RegisterSerializer

User = get_user_model()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all() 
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
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            
            return Response({
                'message': 'User registered and logged in successfully',
                'access_token': access_token,
                'refresh_token': refresh_token 
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def post(self, request):
        # username = request.data.get('username')
        # password = request.data.get('password')
        
        # if User.objects.filter(username=username).exists():
        #     return Response({"error": "This username is already taken"}Ч,
        #                     status=status.HTTP_400_BAD_REQUEST)
        # user = User.objects.create(username=username, password=password)
        # return Response({"message": "User created"}, 
        #                 status=status.HTTP_201_CREATED)
        
        # serializer = RegisterSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
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
    
        

    

