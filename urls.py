from django.urls import path
from . import views

urlpatterns = [
    path('khk2/',views.index,name="index"),
]