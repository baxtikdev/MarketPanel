# Generated by Django 4.0.5 on 2022-06-27 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_products_discount_alter_card_sold_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='payment',
            field=models.CharField(blank=True, choices=[('Naqd', 'Naqd'), ('Click', 'Click'), ('UzCard', 'UzCard'), ('Humo', 'Humo'), ('PaymeGo', 'PaymeGo')], max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='SaleHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sold_price', models.FloatField(default=0, null=True)),
                ('products', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.products')),
                ('sale', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.sale')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.casher')),
            ],
        ),
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_price', models.FloatField(default=0)),
                ('changed_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.products')),
            ],
        ),
    ]