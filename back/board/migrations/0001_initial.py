# Generated by Django 4.2 on 2023-06-19 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("user", models.CharField(max_length=200)),
                ("message", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "board",
            },
        ),
    ]
