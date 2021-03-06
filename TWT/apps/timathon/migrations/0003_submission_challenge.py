# Generated by Django 3.1.1 on 2020-09-28 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0008_auto_20200929_0004"),
        ("timathon", "0002_team_votes"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="challenge",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="challenges.challenge",
            ),
            preserve_default=False,
        ),
    ]
