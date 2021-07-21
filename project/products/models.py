from django.db import models

# модели - таблицы

class ProductCategory(models.Model):
    name = models.CharField(max_length=64,unique=True)
    description = models.TextField(blank=True)
