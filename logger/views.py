from django.shortcuts import render

from rest_framework import viewsets

from logger.serializers import CustomersSerializer
from logger.models import Customers


class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all().order_by('first_name')
    serializer_class = CustomersSerializer
