# Generated by Django 4.1.7 on 2023-04-13 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("register", "0002_delete_userregister"),
    ]

    operations = [
        migrations.CreateModel(
            name="TeamRegister",
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
                ("team_name", models.CharField(max_length=100)),
                ("team_size", models.IntegerField()),
                ("college_name", models.CharField(max_length=100)),
                ("person1", models.CharField(max_length=100)),
                ("person2", models.CharField(max_length=100)),
                ("person3", models.CharField(max_length=100)),
                ("person4", models.CharField(max_length=100)),
                ("leader_name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
