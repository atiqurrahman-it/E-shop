# Generated by Django 3.2.4 on 2021-06-18 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppShopStore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AppShopStore.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sort_description',
            field=models.CharField(default='', max_length=265, null=True, verbose_name='sort_description'),
        ),
    ]
