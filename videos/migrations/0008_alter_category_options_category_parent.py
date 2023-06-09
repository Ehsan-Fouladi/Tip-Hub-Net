# Generated by Django 4.1.3 on 2023-05-09 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_category_video_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created'], 'verbose_name': 'دست بندی', 'verbose_name_plural': 'دست بندی ها'},
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='videos.category'),
            preserve_default=False,
        ),
    ]
