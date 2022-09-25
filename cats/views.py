from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from cats.serializers import CategoryTreeSerializer, CategorySerializer
from cats.models import CategoryTree, Category

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the Categories index.")


class CategoryTreeViewSet(viewsets.ModelViewSet):
    queryset = CategoryTree.objects.all()
    serializer_class = CategoryTreeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
