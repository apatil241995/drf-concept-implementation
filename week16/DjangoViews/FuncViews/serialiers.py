from rest_framework import serializers
from .models import EmployeeData

"""
this is the serializer model serializer is used here for serializing the Employee data
"""


class FuncViewsSerializer(serializers.Modelserializer):
    class Meta:
        model = EmployeeData
        fields = "__all__"
