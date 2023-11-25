from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.price}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(f'{self.name}-{self.price}')
        return super().save()
