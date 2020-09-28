# Generated by Django 3.1.1 on 2020-09-28 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenges', '0007_challenge_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('invite', models.CharField(default=uuid.uuid4, editable=False, help_text='invite', max_length=255, unique=True)),
                ('name', models.TextField(help_text='Name of the team', max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('winner', models.BooleanField(default=False)),
                ('submitted', models.BooleanField(default=False)),
                ('challenge', models.ForeignKey(help_text='Code Jam', on_delete=django.db.models.deletion.CASCADE, to='challenges.challenge')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(help_text='A Submission ID, automatically generated by Postgres.', primary_key=True, serialize=False)),
                ('github_link', models.URLField(help_text='Link to github repo', max_length=150)),
                ('description', models.TextField(help_text='Project Description', max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timathon.team')),
            ],
        ),
    ]