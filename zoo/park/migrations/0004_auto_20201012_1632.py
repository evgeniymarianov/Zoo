# Generated by Django 3.1.2 on 2020-10-12 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0003_auto_20201012_1543'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='space',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AlterField(
            model_name='careperiod',
            name='ended_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
