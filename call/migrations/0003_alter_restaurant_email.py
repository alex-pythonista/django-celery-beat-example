# Generated by Django 4.1.6 on 2024-05-26 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0002_remove_restaurant_phone_restaurant_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
