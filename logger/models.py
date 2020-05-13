from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Customers(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    contact_number = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=500, blank=True)


class Farms(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=False, blank=False)
    farm_name = models.CharField(max_length=100, blank=False)


class Accounts(models.Model):
    PAYMENT_METHOD_CHOICES = [('cash', 'cash'), ('e-money_transfer', 'e-money transfer')]

    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateField(default=date.today(), blank=False, editable=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cash')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    amount_owing = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0)


class Records(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateField(default=date.today(), blank=False, editable=True)
    farm = models.ForeignKey(Farms, on_delete=models.CASCADE, null=False, blank=False)
    start_time = models.TimeField(blank=False, editable=True)
    end_time = models.TimeField(blank=False, editable=True)
    time_difference = models.TimeField(blank=False, editable=False)
    cost = models.DecimalField(blank=False, max_digits=10, decimal_places=2)


class DailyRecords(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateField(default=date.today(), blank=False, editable=True)
    total_uptime = models.TimeField(blank=False, editable=False)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
