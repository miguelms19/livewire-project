# Generated by Django 2.0.2 on 2018-04-04 23:12

from django.db import migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20180403_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=s3direct.fields.S3DirectField(),
        ),
    ]