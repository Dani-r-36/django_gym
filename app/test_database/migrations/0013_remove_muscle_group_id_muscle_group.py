# Generated by Django 4.2.7 on 2023-11-10 16:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test_database', '0012_rename_name_exercise_exercise_name_exercise_machine_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='muscle',
            name='group_id',
        ),
        migrations.AddField(
            model_name='muscle',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='test_database.musclegroup'),
            preserve_default=False,
        ),
    ]
