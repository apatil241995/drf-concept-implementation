from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serialiers import GenViewsSerializer
from .models import CustomerData
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions

"""
view created to get all the student entries
"""


class CustomerList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = CustomerData.objects.all()
    serializer_class = GenViewsSerializer

    def get_queryset(self):
        return self.queryset


"""
view created to create a student entre
"""


class CreateCustomerEntry(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = CustomerData.objects.all()
    serializer_class = GenViewsSerializer

    def perform_create(self, serializer):
        return serializer.save()


"""
view created to update a student entre
"""


class UpdateCustomerEntry(generics.UpdateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = CustomerData.objects.all()
    serializer_class = GenViewsSerializer
    lockup_field = 'id'

    def perform_update(self, serializer):
        return serializer.save(self.request.data)


"""
view created to delete a  student entre
"""


class DeleteCustomerEntry(generics.DestroyAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = CustomerData.objects.all()
    serializer_class = GenViewsSerializer
    lockup_field = 'id'
