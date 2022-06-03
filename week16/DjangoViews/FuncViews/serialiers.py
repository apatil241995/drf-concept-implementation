from rest_framework import serializers
from .models import EmployeeData


class FuncViewsSerializer(serializers.Modelserializer):
    class Meta:
        model = EmployeeData
        fields = "__all__"
