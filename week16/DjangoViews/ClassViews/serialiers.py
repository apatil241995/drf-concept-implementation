from rest_framework import serializers
from .models import StudentData

"""
this is the serializer model serializer is used here for serializing the student data
"""


class ClassViewsSerializer(serializers.Modelserializer):
    class Meta:
        model = StudentData
        fields = "__all__"
