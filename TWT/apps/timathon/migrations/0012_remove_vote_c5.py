# Generated by Django 3.2.3 on 2021-06-03 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timathon', '0011_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='c5',
        ),
    ]
