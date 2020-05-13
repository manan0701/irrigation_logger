from rest_framework import serializers

from logger.models import Customers


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'
