from django.db import models


class StudentData(models.Model):
    s_name = models.CharField(max_length=200)
    s_mobile_no = models.IntegerField()
    view_type = models.CharField(max_length=100)
