from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Category, Product, Order, OrderProduct


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = '__all__'
        
    def get_orders(self, obj):
        user_orders = Order.objects.filter(user=obj)
        return OrderSerializer(user_orders, many=True).data

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
        fields = ['id', 'user', 'created_at', 'full_name', 'email', 'phone', 'delivery_address','comment', 'products', 'items']
        read_only_fields = ['user', 'created_at']
        
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        # user = self.context['request'].user
        # order = Order.objects.create(user=user, **validated_data)
        order = Order.objects.create(**validated_data) 
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
    
class CartItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(write_only=True)
    product = ProductSerializer(read_only=True)
    quantity = serializers.IntegerField(min_value=1)
    user_id = serializers.IntegerField(allow_null=True)
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        try:
            product = Product.objects.get(id=instance['product_id'])
            ret['product'] = ProductSerializer(product, context=self.context).data
        except Product.DoesNotExist:
            ret['product'] = None
        return ret