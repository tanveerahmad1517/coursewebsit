# Generated by Django 2.0 on 2018-04-06 08:51

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0021_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='media/default.png', upload_to=courses.models.get_image_path),
        ),
    ]
