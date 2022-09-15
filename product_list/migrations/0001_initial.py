# Generated by Django 4.1.1 on 2022-09-15 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=50)),
                ('brand', models.CharField(default='', max_length=50)),
                ('descriptions', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('count', models.IntegerField()),
                ('size_s', models.IntegerField(default=0)),
                ('size_m', models.IntegerField(default=0)),
                ('size_l', models.IntegerField(default=0)),
                ('size_xl', models.IntegerField(default=0)),
                ('size_xxl', models.IntegerField(default=0)),
                ('discount', models.FloatField(default=0)),
                ('colour', models.CharField(default='', max_length=50)),
                ('img', models.ImageField(default='', upload_to='product_list/images')),
                ('rating', models.FloatField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.category')),
            ],
        ),
    ]
