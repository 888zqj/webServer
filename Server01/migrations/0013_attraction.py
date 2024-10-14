# Generated by Django 5.1.1 on 2024-10-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Server01", "0012_image_height_image_width"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attraction",
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
                ("city", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=200)),
                ("location", models.TextField()),
                ("distance", models.TextField()),
                ("coordinate", models.TextField()),
                ("comment_num", models.TextField()),
                ("comment_score", models.TextField()),
                ("hot_comment_score", models.TextField()),
                ("picture", models.TextField()),
                ("free_or_not", models.TextField()),
                ("price", models.TextField()),
                ("pre_price", models.TextField()),
                ("class_information", models.TextField()),
                ("tag", models.TextField()),
                ("five_a_or_not", models.TextField()),
                ("description", models.TextField()),
            ],
        ),
    ]
