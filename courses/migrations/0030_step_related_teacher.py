# Generated by Django 2.0 on 2018-04-07 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0029_auto_20180407_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='related_teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='related_teahcers', to='courses.Teacher'),
            preserve_default=False,
        ),
    ]
