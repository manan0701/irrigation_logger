# Generated by Django 3.0.6 on 2020-05-18 06:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('contact_number', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.IntegerField()),
                ('date', models.DateField(default=datetime.date(2020, 5, 18))),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('time_difference', models.TimeField(editable=False)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logger.Customers')),
            ],
        ),
        migrations.CreateModel(
            name='Farms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_name', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logger.Customers')),
            ],
        ),
        migrations.CreateModel(
            name='DailyRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2020, 5, 18))),
                ('total_uptime', models.TimeField(editable=False)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logger.Customers')),
            ],
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2020, 5, 18))),
                ('payment_method', models.CharField(choices=[('cash', 'cash'), ('e-money_transfer', 'e-money transfer')], default='cash', max_length=20)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('amount_owing', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logger.Customers')),
            ],
        ),
    ]
