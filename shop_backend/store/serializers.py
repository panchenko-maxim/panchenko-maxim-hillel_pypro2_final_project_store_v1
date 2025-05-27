from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Category, Product, Order, OrderProduct


User = get_user_model()


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
        

class OrderProductInputSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    
class OrderProductOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['id', 'product', 'quantity', 'order']

class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductOutputSerializer(source='orderproduct_set', many=True, read_only=True)
    items = OrderProductInputSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'comment', 'products', 'items']
        
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user
        order = Order.objects.create(user=user, **validated_data)
        for item in items_data:
            OrderProduct.objects.create(
                order=order,
                product_id=item['product_id'],
                quantity=item['quantity']
            )
        return order
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user