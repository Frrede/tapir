# Generated by Django 3.2.16 on 2023-02-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shifts", "0043_auto_20230508_1821"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shiftuserdata",
            name="attendance_mode",
            field=models.CharField(
                choices=[
                    ("regular", "🏠 ABCD"),
                    ("flying", "✈ Flying"),
                    ("frozen", "❄ Frozen"),
                ],
                default="regular",
                max_length=32,
                verbose_name="Shift system",
            ),
        ),
    ]