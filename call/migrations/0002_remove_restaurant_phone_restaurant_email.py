# Generated by Django 4.1.6 on 2024-05-26 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='phone',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='email',
            field=models.EmailField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
