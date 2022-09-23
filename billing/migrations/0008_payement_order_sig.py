# Generated by Django 4.1.1 on 2022-09-22 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('billing', '0007_alter_order_payment_history_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='payement_order_sig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_payment_id', models.CharField(max_length=100)),
                ('razorpay_order_id', models.CharField(max_length=100)),
                ('razorpay_signature', models.CharField(max_length=100)),
                ('buy_now', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
