from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category name"


class Recept(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Product")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)
    time_cooking = models.DecimalField(default=25, max_digits=8, decimal_places=2)
    ingrediens = models.TextField(default='', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="photo/%Y/%m/%d", verbose_name="Photo")

    def get_absolute_url(self):
        return reverse('product_form_update', kwargs={'product_id': self.pk})
    # product_form_update - свянан с урлом, урл связан с апдейт вьюхой.

    def __str__(self):
        return f'{self.name} / {self.category} / {self.time_cooking}'

    class Meta:
        verbose_name = "Product name"






