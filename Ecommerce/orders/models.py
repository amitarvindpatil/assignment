from django.db import models
from User_Profile.models import UserProfile
# from django.conf import settings
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.product_name


class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name='product',
                                on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.id)

#
class Order(models.Model):
    orderitem = models.ForeignKey(OrderItem, related_name='order',
                                 on_delete=models.CASCADE)
    order_st = [
        ('Order Placed', 'Order Placed'),
        ('Order Accepted', 'Order Accepted'),
        ('Order Canceled', 'Order Canceled'),
    ]

    order_status = models.CharField(
        max_length=20, choices=order_st)

#     user_data = models.ForeignKey(settings.AUTH_USER_MODEL,
#                                 on_delete=models.CASCADE)
# #
    def __str__(self):
        return str(self.orderitem)
