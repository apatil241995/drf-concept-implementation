from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serialiers import GenViewsSerializer
from .models import CustomerData


class CustomerList(generics.ListAPIView):
    queryset = CustomerData.objects.all()
    serializer_class = GenViewsSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return self.queryset


class CreateCustomerEntry(generics.CreateAPIView):
    queryset = CustomerData.objects.all()
    serializer_class = GenViewsSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        return serializer.save()


class UpdateCustomerEntry(generics.UpdateAPIView):
    queryset = CustomerData.objects.all()
    serializer_class = GenViewsSerializer
    permission_classes = [IsAdminUser]
    lockup_field = 'id'

    def perform_update(self, serializer):
        return serializer.save(self.request.data)


class DeleteCustomerEntry(generics.DestroyAPIView):
    queryset = CustomerData.objects.all()
    serializer_class = GenViewsSerializer
    permission_classes = [IsAdminUser]
