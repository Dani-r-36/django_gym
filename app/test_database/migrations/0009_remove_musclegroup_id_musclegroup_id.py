# Generated by Django 4.2.7 on 2023-11-06 15:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test_database', '0008_alter_musclegroup_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musclegroup',
            name='id',
        ),
        migrations.AddField(
            model_name='musclegroup',
            name='ID',
            field=models.AutoField(db_column='group_id', primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
