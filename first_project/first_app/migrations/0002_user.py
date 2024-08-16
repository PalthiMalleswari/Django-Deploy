# Generated by Django 4.1 on 2024-08-15 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("first_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100, unique=True)),
                ("last_name", models.CharField(max_length=100, unique=True)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
