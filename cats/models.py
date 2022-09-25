from django.db import models


# Create your models here.

class CategoryTree(models.Model):
    category_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    similar_to = models.CharField(max_length=200, null=True, blank=True)


class Category(models.Model):
    category_tree = models.ForeignKey(CategoryTree, on_delete=models.CASCADE)
    category_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    similar_to = models.CharField(max_length=200, null=True, blank=True)
