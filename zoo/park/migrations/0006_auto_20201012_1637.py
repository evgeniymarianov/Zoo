# Generated by Django 3.1.2 on 2020-10-12 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0005_auto_20201012_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careperiod',
            name='ended_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
