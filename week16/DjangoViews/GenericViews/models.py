from django.db import models

"""
Basic model is created to store customer data which contains fields like customer name as c_name
and customer mobile no as c_mobile_no and view_type to store what type of view is used to do the
curd operations
"""


class CustomerData(models.Model):
    c_name = models.CharField(max_length=200)
    c_mobile_no = models.IntegerField()
    view_type = models.CharField(max_length=100)
