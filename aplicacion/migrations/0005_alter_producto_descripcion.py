# Generated by Django 5.0.6 on 2024-06-26 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_alter_producto_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
    ]
