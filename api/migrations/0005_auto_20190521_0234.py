# Generated by Django 2.2.1 on 2019-05-21 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190521_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopic',
            name='uuid',
            field=models.CharField(default='5320a814-c147-446f-9e47-02466060935c', max_length=60),
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='aa29d80c-989c-4578-8bea-f8e99dc2f969', max_length=60, unique=True),
        ),
    ]
