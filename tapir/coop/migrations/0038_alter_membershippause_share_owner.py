# Generated by Django 3.2.21 on 2023-10-23 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "coop",
            "0037_membershippause_membershippausecreatedlogentry_membershippauseupdatedlogentry",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="membershippause",
            name="share_owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="coop.shareowner",
                verbose_name="Member",
            ),
        ),
    ]
