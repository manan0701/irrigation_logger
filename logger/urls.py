from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from logger.views import CustomersViewSet, RecordsViewSet

router = routers.DefaultRouter()
router.register(r'customers', viewset=CustomersViewSet)
router.register(r'records', viewset=RecordsViewSet)

urlpatterns = router.urls
