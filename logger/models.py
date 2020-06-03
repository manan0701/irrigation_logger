from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Customers(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    middle_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    contact_number = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + '' + self.last_name


class Farms(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=False, blank=False)
    farm_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.farm_name


class Accounts(models.Model):
    PAYMENT_METHOD_CHOICES = [('cash', 'cash'), ('e-money_transfer', 'e-money transfer')]

    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateField(default=date.today(), null=False, editable=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cash')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    amount_owing = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)


class Records(models.Model):
    date = models.DateField(default=date.today(), null=False, editable=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=False, blank=False)

    # farm_name = models.ForeignKey(Farms, on_delete=models.CASCADE, null=False, blank=False)
    start_time = models.TimeField(null=False, editable=True)
    end_time = models.TimeField(null=False, editable=True)
    time_difference = models.TimeField(null=True, editable=False)
    cost = models.DecimalField(null=True, max_digits=10, decimal_places=2)


class DailyRecords(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateField(default=date.today(), null=False, editable=True)
    total_uptime = models.TimeField(null=False, editable=False)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
