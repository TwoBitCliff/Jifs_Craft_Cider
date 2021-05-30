from django.db import models
from profiles.models import UserProfile
# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    name = models.CharField(max_length=254)
    product_id = models.CharField(max_length=254, null=True, blank=True)
    brand = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    quantity = models.CharField(max_length=254)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    class Meta:
        ordering = ['created_on']
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,
                                   related_name='reviews')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='reviews')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.body
