# Generated by Django 4.1.3 on 2023-05-08 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_remove_video_views'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-created'], 'verbose_name': 'ویدیو ها', 'verbose_name_plural': 'ویدیو'},
        ),
    ]
