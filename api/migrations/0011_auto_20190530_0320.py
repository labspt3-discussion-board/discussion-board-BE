# Generated by Django 2.2.1 on 2019-05-30 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20190530_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopic',
            name='uuid',
            field=models.CharField(default='1fd752b3-9e74-4181-9ae8-070dee7f3e76', max_length=60),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='455a9ac5-7aa8-41d7-8bdf-cd5c2454499f', max_length=60, unique=True),
        ),
    ]