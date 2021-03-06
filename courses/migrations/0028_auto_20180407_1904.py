# Generated by Django 2.0 on 2018-04-07 14:04

import courses.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0027_remove_course_step_detail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={},
        ),
        migrations.RenameField(
            model_name='step',
            old_name='course',
            new_name='related_course',
        ),
        migrations.RenameField(
            model_name='step',
            old_name='description',
            new_name='related_title',
        ),
        migrations.RemoveField(
            model_name='step',
            name='contents',
        ),
        migrations.RemoveField(
            model_name='step',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='step',
            name='title',
        ),
        migrations.AddField(
            model_name='step',
            name='related_created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='step',
            name='related_description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='step',
            name='related_image',
            field=models.ImageField(default='media/default.png', upload_to=courses.models.get_image_path),
        ),
        migrations.AddField(
            model_name='step',
            name='related_title_html',
            field=models.TextField(default=django.utils.timezone.now, editable=False),
            preserve_default=False,
        ),
    ]
