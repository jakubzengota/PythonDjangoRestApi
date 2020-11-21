from django.db import models

#Categories
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=300)

#Articles
class Article(models.Model):
    categories = models.ManyToManyField(Category, blank=True)
    name = models.CharField(max_length=500)
    description = models.TextField()