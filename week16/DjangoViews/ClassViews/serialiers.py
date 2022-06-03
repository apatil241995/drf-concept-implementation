from rest_framework import serializers
from .models import StudentData


class ClassViewsSerializer(serializers.Modelserializer):
    class Meta:
        model = StudentData
        fields = "__all__"
