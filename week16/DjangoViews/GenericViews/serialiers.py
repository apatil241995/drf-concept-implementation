from rest_framework import serializers
from .models import CostumerData


class GenViewsSerializer(serializers.Modelserializer):
    class Meta:
        model = CostumerData
        fields = "__all__"
