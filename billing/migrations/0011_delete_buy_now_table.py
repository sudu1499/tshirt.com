# Generated by Django 4.1.1 on 2022-09-23 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0010_buy_now_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='buy_now_table',
        ),
    ]
