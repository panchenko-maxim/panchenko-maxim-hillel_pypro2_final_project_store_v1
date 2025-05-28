from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer

User = get_user_model()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    # queryset = Order.objects.all()
    
    def get_queryset(self):
        qs = Order.objects.filter(user=self.request.user)
        return qs
    
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
    
    
    

