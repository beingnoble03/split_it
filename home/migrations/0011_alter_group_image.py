# Generated by Django 4.0.1 on 2022-03-10 08:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_totaltransaction_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
