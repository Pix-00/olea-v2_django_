# Generated by Django 2.2.1 on 2019-05-12 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(blank=True, max_length=40, null=True)),
                ('qq', models.CharField(blank=True, max_length=11, null=True)),
                ('line', models.CharField(blank=True, max_length=30, null=True)),
                ('groups', models.CharField(blank=True, default='', max_length=30)),
                ('cancelled_count', models.IntegerField(default=0)),
                ('last_access', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
