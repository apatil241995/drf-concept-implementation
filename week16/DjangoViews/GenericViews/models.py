from django.db import models


class CustomerData(models.Model):
    c_name = models.CharField(max_length=200)
    c_mobile_no = models.IntegerField()
    view_type = models.CharField(max_length=100)
