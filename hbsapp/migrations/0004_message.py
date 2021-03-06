# Generated by Django 3.2 on 2021-04-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hbsapp', '0003_roombooking_paid_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
