# Generated by Django 2.0 on 2018-04-07 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0026_course_step_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='step_detail',
        ),
    ]
