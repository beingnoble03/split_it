# Generated by Django 4.0.1 on 2022-01-20 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_group_details_transaction_details_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='topic',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='topic',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
