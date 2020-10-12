# Generated by Django 3.1.2 on 2020-10-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='careperiod',
            options={'verbose_name': 'Период ухода', 'verbose_name_plural': 'Периоды ухода'},
        ),
        migrations.AlterModelOptions(
            name='placementperiod',
            options={'verbose_name': 'Период размещения', 'verbose_name_plural': 'Периоды размещения'},
        ),
        migrations.AlterField(
            model_name='careperiod',
            name='ended_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='space',
            name='type',
            field=models.CharField(choices=[('Cage', 'Cage'), ('Enclosure', 'Enclosure'), ('Terrarium', 'Terrarium')], max_length=15, verbose_name='Тип помещения'),
        ),
    ]