# Generated by Django 3.2.15 on 2022-09-10 08:05

import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0004_auto_20211003_0941'),
        ('shifts', '0038_auto_20220821_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateExemptionLogEntry',
            fields=[
                ('logentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='log.logentry')),
                ('old_values', django.contrib.postgres.fields.hstore.HStoreField()),
                ('new_values', django.contrib.postgres.fields.hstore.HStoreField()),
            ],
            options={
                'abstract': False,
            },
            bases=('log.logentry',),
        ),
    ]
