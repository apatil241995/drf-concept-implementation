from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_no = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Shope(models.Model):
    shop_name = models.CharField(max_length=50)
    shop_owner = models.ForeignKey(Owner, on_delete=models.PROTECT)
    shop_address = models.CharField(max_length=400)


class Items(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_quantity = models.IntegerField()

    def __str__(self):
        return self.item_name


class Sales(models.Model):
    item_sold = models.CharField(max_length=50)
    sold_at = models.DateTimeField(auto_now_add=True, blank=True)
