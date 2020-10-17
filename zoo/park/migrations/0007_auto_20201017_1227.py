# Generated by Django 3.1.2 on 2020-10-17 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0006_auto_20201012_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='animals', to='park.category', verbose_name='Категория'),
        ),
    ]
