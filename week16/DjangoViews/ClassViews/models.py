from django.db import models

"""
Basic model is created to store student data which contains fields like student name as s_name
and student mobile no as s_mobile_no and view_type to store what type of view is used to do the
curd operations
"""


class StudentData(models.Model):
    s_name = models.CharField(max_length=200)
    s_mobile_no = models.IntegerField()
    view_type = models.CharField(max_length=100)
