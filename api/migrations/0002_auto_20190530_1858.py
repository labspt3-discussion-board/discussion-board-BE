# Generated by Django 2.2.1 on 2019-05-30 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='uuid',
            field=models.CharField(default='072b9eef-39a4-488c-94a7-f083cf70697e', max_length=60),
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='dd2b63b5-1e44-4efa-bd20-7becc9dce6b5', max_length=60, unique=True),
        ),
    ]