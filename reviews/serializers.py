from rest_framework import serializers
from .models import Review, Product

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['prod_num', 'rating', 'verbage']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']