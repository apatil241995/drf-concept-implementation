from rest_framework import serializers
from .models import CustomerData

"""
this is the serializer model serializer is used here for serializing the customer data
"""


class GenViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerData
        fields = "__all__"
