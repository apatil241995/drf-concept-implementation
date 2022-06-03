from django.db import models


class EmployeeData(models.Model):
    e_name = models.CharField(max_length=200)
    e_mobile_no = models.IntegerField()
    view_type = models.CharField(max_length=100)
