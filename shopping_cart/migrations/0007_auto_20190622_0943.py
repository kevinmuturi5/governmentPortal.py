# Generated by Django 2.2 on 2019-06-22 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0006_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
