# Generated by Django 2.0.4 on 2018-04-20 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_player_posicion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='posicion',
            field=models.CharField(choices=[('Base', 'Base'), ('Escolta', 'Escolta'), ('Alero', 'Alero'), ('Alero-pivot', 'Ala-pivot'), ('Pivot', 'Pivot')], default='Base', max_length=200),
        ),
    ]
