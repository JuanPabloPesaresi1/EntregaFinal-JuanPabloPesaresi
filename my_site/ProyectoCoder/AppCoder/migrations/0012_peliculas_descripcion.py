# Generated by Django 4.0.5 on 2022-07-22 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0011_remove_peliculas_precioentrada'),
    ]

    operations = [
        migrations.AddField(
            model_name='peliculas',
            name='descripcion',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
