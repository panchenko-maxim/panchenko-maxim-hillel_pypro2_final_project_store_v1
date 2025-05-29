from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
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

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all() 
    permission_classes = [IsAuthenticated] 
        
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all().order_by('-created_at')
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         # >>> ДОБАВЬТЕ ЭТИ СТРОКИ ДЛЯ ОТЛАДКИ <<<
#         print("Received request data (from request.data):", request.data)
#         print("Received request data (from request.POST):", request.POST) # на всякий случай, если это форма
#         # >>> ------------------------------ <<<

#         serializer = self.get_serializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if User.objects.filter(username=username).exists():
            return Response({"error": "This username is already taken"},
                            status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(username=username, password=password)
        return Response({"message": "User created"}, 
                        status=status.HTTP_201_CREATED)
        
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
    
        

    

