# Generated by Django 2.0 on 2018-04-06 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_auto_20180406_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(default='Select Teacher', on_delete=django.db.models.deletion.CASCADE, related_name='teahcers', to='courses.Teacher'),
        ),
    ]
