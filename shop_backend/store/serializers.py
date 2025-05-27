from rest_framework import serializers
from .models import Category, Product, Order, OrderProduct

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(source='ordeproduct_set', many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'products']