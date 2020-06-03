from rest_framework import serializers

from logger.models import Customers, Records


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super(RecordsSerializer, self).to_representation(instance)
    #     representation['farm'] = str(instance.farm)
    #     representation['customer'] = str(instance.customer)
    #     return representation
