# Generated by Django 4.1.3 on 2023-05-10 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_alter_category_options_category_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]
