from rest_framework import serializers
from .models import CustomerData


class GenViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerData
        fields = "__all__"
