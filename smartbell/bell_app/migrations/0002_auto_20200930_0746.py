# Generated by Django 2.2.1 on 2020-09-29 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bell_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
