# Generated by Django 3.0.2 on 2020-02-21 17:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 2, 21, 17, 13, 53, 130300, tzinfo=utc))),
                ('publications', models.ManyToManyField(to='gra_blog.Publication')),
            ],
            options={
                'ordering': ('headline',),
            },
        ),
    ]
