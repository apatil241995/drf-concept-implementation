from django.urls import path
from . import views
urlpatterns = [
    path("create/", views.CreateCustomerEntry.as_view()),
    path("getDetails/", views.CustomerList.as_view()),
    path("update/", views.UpdateCustomerEntry.as_view()),
    path("delete/", views.DeleteCustomerEntry.as_view()),
]