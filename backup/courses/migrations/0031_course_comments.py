# Generated by Django 2.0.5 on 2018-06-17 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0030_step_related_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='comments',
            field=models.IntegerField(default=0),
        ),
    ]
