from rest_framework import serializers

from cats.models import CategoryTree, Category

class CategoryTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTree
        fields = ('category_id', 'name', 'description', 'image', 'similar_to')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_tree', 'category_id', 'name', 'description', 'image', 'similar_to')