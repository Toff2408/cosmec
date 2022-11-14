
from django.db import models
from django.contrib.auth.models import User
from mainapp.models import Product

# Create your models here.

class Shopcart(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    item_carted = models.IntegerField(default = 1)
    amount = models.FloatField(default=1.0)
    cart_no = models.CharField(max_length = 50)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
            db_table = 'shopcart'
            managed = True
            verbose_name = 'Shopcart'
            verbose_name_plural = 'Shopcarts'



STATUS = [
    ('New','New'),
    ('Processing', 'Processing'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered')
]


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    total = models.FloatField(default=1.0)
    cart_no = models.CharField(max_length = 50)
    pay_code = models.CharField(max_length = 50)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length = 50, choices=STATUS, default='NEW' )
    created = models.DateTimeField(auto_now_add=True)
    admin_note = models.TextField(max_length = 50)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
            db_table = 'payment'
            managed = True
            verbose_name = 'payment'
            verbose_name_plural = 'payments'



class Shipping(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, default = 2)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50, default = 'A')
    phone = models.IntegerField(default = 0)
    delivery_address = models.CharField(max_length = 50, default="a")
    billing_address = models.CharField(max_length = 50, default='a')
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
