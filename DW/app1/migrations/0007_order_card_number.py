# Generated by Django 5.1.7 on 2025-05-26 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_order_created_at_order_email_order_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='card_number',
            field=models.CharField(default='1234123412341234', max_length=19),
            preserve_default=False,
        ),
    ]
