# Generated by Django 2.2.7 on 2019-12-05 17:33

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebMap', '0003_auto_20191204_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('userpassword', models.CharField(max_length=100)),
                ('userLocation', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
