from django.db import models

"""
Basic model is created to store employee data which contains fields like employee name as e_name
and employee mobile no as e_mobile_no and view_type to store what type of view is used to do the
curd operations
"""


class EmployeeData(models.Model):
    e_name = models.CharField(max_length=200)
    e_mobile_no = models.IntegerField()
    view_type = models.CharField(max_length=100)
