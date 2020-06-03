from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from logger.serializers import CustomersSerializer, RecordsSerializer
from logger.models import Customers, Records


class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all().order_by('first_name')
    serializer_class = CustomersSerializer


class RecordsViewSet(viewsets.ModelViewSet):
    queryset = Records.objects.all()
    serializer_class = RecordsSerializer


@api_view(['GET', 'POST'])
def get_records(request):
    if request.method == 'GET':
        data = Records.objects.all()

        serializer = RecordsSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
