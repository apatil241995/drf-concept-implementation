from django.urls import path,include
from . import views
urlpatterns = [
    path("create/", views.postEmployee_data),
    path("getDetails/", views.getEmployee_data),
    path("update/", views.updateEmployee_data),
    path("delete/", views.deleteEmployee_data),
]