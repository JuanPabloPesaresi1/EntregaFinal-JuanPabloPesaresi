# Generated by Django 4.0.5 on 2022-07-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_alter_tienda_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tienda',
            name='precio',
            field=models.IntegerField(verbose_name='Precio $'),
        ),
    ]
