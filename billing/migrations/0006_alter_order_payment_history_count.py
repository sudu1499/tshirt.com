# Generated by Django 4.1.1 on 2022-09-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0005_alter_checkout_product_id_alter_checkout_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_payment_history',
            name='count',
            field=models.IntegerField(),
        ),
    ]
