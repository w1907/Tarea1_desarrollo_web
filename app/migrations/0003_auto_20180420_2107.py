# Generated by Django 2.0.4 on 2018-04-20 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180420_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='descripcion',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
