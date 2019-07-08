from django.urls import path,include
from . import views

urlpatterns = [
    path("registration1/",views.form,name="registration1")
    path("registeruser/",views.registerUser,name="registeruser")
]