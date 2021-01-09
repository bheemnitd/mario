from django.contrib import admin
from django.urls import path, include
from app import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('api',views.EmployeeCRUDCBV)

urlpatterns = [
    path('', include(router.urls)),
]