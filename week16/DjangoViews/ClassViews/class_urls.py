from django.urls import path,include
from . import views
urlpatterns = [
    path("create/", views.CreateStudentEntries.as_view()),
    path("getDetails/", views.StudentEntries.as_view()),
    path("update/", views.UpdateStudentEntries.as_view()),
    path("delete/", views.DeleteStudentEntries.as_view()),
    path("patch/", views.ParUpdateStudentEntries.as_view()),
]