# Generated by Django 2.0.2 on 2018-04-11 18:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('summary', models.CharField(max_length=2000)),
                ('email', models.CharField(blank=True, max_length=2000, validators=[django.core.validators.URLValidator()])),
            ],
        ),
    ]
