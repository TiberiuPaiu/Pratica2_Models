# Generated by Django 3.1.7 on 2021-03-27 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_auto_20210327_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='talla',
            field=models.PositiveSmallIntegerField(choices=[(1, 'S'), (2, 'M'), (3, 'L'), (4, 'XL'), (5, 'XXL')], default=2),
        ),
    ]
