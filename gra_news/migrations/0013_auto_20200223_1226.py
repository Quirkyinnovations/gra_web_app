# Generated by Django 3.0.2 on 2020-02-23 12:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gra_news', '0012_auto_20200223_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 23, 12, 26, 20, 326962, tzinfo=utc)),
        ),
    ]