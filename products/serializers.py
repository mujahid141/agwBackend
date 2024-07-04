from rest_framework import serializers
from .models import Categories, Promotions, Product,ProductImage
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'title', 'slug', 'description')


class PromotionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotions
        fields = ('id', 'description', 'discount')

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('product', 'image')

class ProductSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer(read_only=True)
    promotions = PromotionsSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'slug', 'title', 'description', 'price', 'inventory', 'last_update',
                  'type_of', 'color', 'shape', 'category', 'promotions', 'date_added', 'origin', 'weight', 'images')

