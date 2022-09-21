# Generated by Django 4.1.1 on 2022-09-21 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product_list', '0001_initial'),
        ('Tshirt_cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('price_of_one', models.FloatField(default=1)),
                ('total_amount', models.FloatField(default=0)),
                ('order_count', models.ForeignKey(db_column='product_count', on_delete=django.db.models.deletion.CASCADE, to='Tshirt_cart.cart')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_list.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='order_payment_history',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField()),
                ('status', models.CharField(default='', max_length=50)),
                ('payment_order_id', models.CharField(default='', max_length=100)),
                ('count', models.ForeignKey(db_column='order_count', on_delete=django.db.models.deletion.DO_NOTHING, to='billing.order')),
                ('prod_id', models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, to='product_list.products')),
                ('user', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
