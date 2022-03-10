# Generated by Django 4.0.1 on 2022-03-09 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_group_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('getter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='totalbackexpenses', to=settings.AUTH_USER_MODEL)),
                ('spender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='totalexpenses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]