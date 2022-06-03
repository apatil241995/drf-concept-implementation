from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from shop_management import models
from shop_management import serializer


class GetPostItems(APIView):

    def get(self, request):
        item_details = models.Items.objects.all()
        items_serialized = serializer.ItemSerializer(item_details, many=True)
        return Response(status=status.HTTP_200_OK, data=items_serialized.data)

    def post(self, request):
        req_data = request.data
        items_serialized = serializer.ItemSerializer(data=req_data)
        if items_serialized.is_valid():
            items_serialized.save()
            return Response(status=status.HTTP_201_CREATED, data=items_serialized.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=items_serialized.errors)


class GetPutDeleteItems(APIView):
    def get(self, request, id):
        item_details = models.Items.objects.get(id=id)
        items_serialized = serializer.ItemSerializer(item_details, many=True)
        return Response(status=status.HTTP_200_OK, data=items_serialized.data)

    def put(self, request, id):
        req_data = request.data
        item_details = models.Items.objects.get(id=id)
        items_serialized = serializer.ItemSerializer(item_details, data=req_data)
        if items_serialized.is_valid():
            items_serialized.save()
            return Response(status=status.HTTP_201_CREATED, data=items_serialized.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=items_serialized.errors)

    def delete(self, request, id):
        item_details = models.Items.objects.get(id=id)
        item_details.delete()
        return Response(status=status.HTTP_200_OK)


class GetPostOwner(APIView):
    def get(self, request):
        owner_details = models.Owner.objects.all()
        owner_serialized = serializer.ShopOwnerSerializer(owner_details, many=True)
        return Response(status=status.HTTP_200_OK, data=owner_serialized)

    def post(self, request):
        req_data = request.data
        owner_serialized = serializer.ShopOwnerSerializer(data=req_data)
        if owner_serialized.is_valid():
            owner_serialized.save()
            return Response(status=status.HTTP_201_CREATED, data=owner_serialized.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=owner_serialized.errors)

    def delete(self, request, id):
        owner_details = models.Owner.objects.get(id=id)
        owner_details.delete()
        return Response(status=status.HTTP_200_OK)


class GetPutDeleteShopOwner(APIView):
    def get(self, request, id):
        shop_details = models.Shop.objects.all()
        shop_serialized = serializer.ShopSerializer(shop_details, many=True)
        return Response(status=status.HTTP_200_OK, data=shop_serialized.data)

    def put(self, request, id):
        req_data = request.data
        shop_details = models.Shop.objects.get(id=id)
        shop_serialized = serializer.ShopSerializer(shop_details, data=req_data)
        if shop_serialized.is_valid():
            shop_details.save()
            return Response(status=status.HTTP_200_OK, data=shop_serialized.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=shop_serialized.errors)


class BuyItem(APIView):
    def post(self, request, str):
        item_details = models.Items.objects.get(item_name=str)
        item_details.item_quantity += 1
        item_details.save()
        return Response(status=status.HTTP_200_OK, data={'item': 'bought'})


class SaleItem(APIView):
    def post(self, request, str):
        item_details = models.Items.objects.get(item_name=str)
        sales_data = serializer.SaleSerializer(data={'item_sold':str})
        if sales_data.is_valid():
            sales_data.save()
        item_details.item_quantity -= 1
        item_details.save()
        return Response(status=status.HTTP_200_OK, data={'item': 'sold'})
