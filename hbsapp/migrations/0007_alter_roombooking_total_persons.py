# Generated by Django 3.2 on 2021-04-22 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hbsapp', '0006_auto_20210422_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roombooking',
            name='total_persons',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
    ]
