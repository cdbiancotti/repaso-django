# Generated by Django 4.0.3 on 2022-04-09 13:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profesionales', '0002_cerrajero_tarjeta_presentacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cerrajero',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
