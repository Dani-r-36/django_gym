# Generated by Django 4.2.7 on 2023-11-15 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_database', '0020_currentlift_exercisedetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='exercise_details',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercise_details', to='test_database.exercisedetails'),
        ),
    ]
