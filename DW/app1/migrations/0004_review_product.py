# Generated by Django 5.1.7 on 2025-05-18 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='app1.product'),
        ),
    ]
