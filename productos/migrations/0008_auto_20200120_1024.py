# Generated by Django 3.0.2 on 2020-01-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_auto_20200119_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenproducto',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
    ]
