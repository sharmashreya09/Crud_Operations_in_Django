from django.urls import path
from .views import Home,Add_Student,Delete_Student,Edit_Student

urlpatterns = [
    path('',Home.as_view(),name="home"),
    path('add/',Add_Student.as_view(),name="addStudent"),
    path('delete/',Delete_Student.as_view(),name="deleteStudent"),
    path('edit/<int:id>/',Edit_Student.as_view() ,name="edit_student")

]