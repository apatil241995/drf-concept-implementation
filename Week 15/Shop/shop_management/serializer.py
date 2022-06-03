from rest_framework import serializers
from shop_management import models


class ItemSerializer(serializers.Serializer):
    item_name = serializers.CharField(max_length=100)
    item_price = serializers.IntegerField()
    item_quantity = serializers.IntegerField()


class ShopOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Owner
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sales
        fields = '__all__'
