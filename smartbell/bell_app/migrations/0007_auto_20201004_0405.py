# Generated by Django 2.2.1 on 2020-10-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bell_app', '0006_auto_20201004_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_hot_ice',
            field=models.CharField(max_length=50),
        ),
    ]
