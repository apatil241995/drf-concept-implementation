from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serialiers import GenViewsSerializer
from .models import CustomerData
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions


class CustomerList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = CustomerData.objects.all()
    serializer_class = GenViewsSerializer

    def get_queryset(self):
        return self.queryset


class CreateCustomerEntry(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = CustomerData.objects.all()
    serializer_class = GenViewsSerializer

    def perform_create(self, serializer):
        return serializer.save()


class UpdateCustomerEntry(generics.UpdateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = CustomerData.objects.all()
    serializer_class = GenViewsSerializer
    lockup_field = 'id'

    def perform_update(self, serializer):
        return serializer.save(self.request.data)


class DeleteCustomerEntry(generics.DestroyAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = CustomerData.objects.all()
    serializer_class = GenViewsSerializer
    lockup_field = 'id'
