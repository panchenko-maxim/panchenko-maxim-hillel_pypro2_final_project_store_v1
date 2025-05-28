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
        fields = ['id', 'user', 'created_at', 'comment', 'products', 'items']
        
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item in items_data:
            OrderProduct.objects.create(
                order=order,
                product_id=item['product_id'],
                quantity=item['quantity']
            )
        return order