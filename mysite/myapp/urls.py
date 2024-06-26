from django.urls import path
from . import views

app_name="myapp"

urlpatterns = [
    path("",views.index,name='index'),
    path("delete/<int:id>/",views.delete_consume,name="delete"),
    path("profile/",views.profilepage,name="profile"),
    path("register/",views.register,name="register"),
]
