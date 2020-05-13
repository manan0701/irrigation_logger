from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from logger.views import CustomersViewSet

router = routers.DefaultRouter()
router.register(r'customers', viewset=CustomersViewSet)

urlpatterns = router.urls
