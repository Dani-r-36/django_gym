# Generated by Django 4.2.7 on 2023-11-15 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_database', '0021_exercise_exercise_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='exercise_details',
        ),
    ]
