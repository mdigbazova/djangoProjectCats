from django.urls import path, re_path, include

from rest_framework import routers

from cats.views import CategoryTreeViewSet, CategoryViewSet

from . import views


router = routers.DefaultRouter()
router.register(r'category_tree', CategoryTreeViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
]

