# Generated by Django 4.2.7 on 2023-11-15 14:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test_database', '0023_remove_exercisedetails_current_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercisedetails',
            name='current_lift',
        ),
        migrations.AddField(
            model_name='exercisedetails',
            name='current',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='test_database.currentlift'),
            preserve_default=False,
        ),
    ]
