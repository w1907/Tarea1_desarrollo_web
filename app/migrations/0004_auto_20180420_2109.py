# Generated by Django 2.0.4 on 2018-04-20 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180420_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='descripcion',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
