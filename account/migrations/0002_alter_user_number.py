# Generated by Django 4.1.3 on 2023-05-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.CharField(max_length=12, unique=True, verbose_name='شماره تلفن'),
        ),
    ]
