# Generated by Django 4.0.1 on 2022-01-21 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_purchase_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='purchase',
        ),
    ]
