# Generated by Django 4.2.7 on 2023-11-13 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_database', '0014_remove_exercise_machine_remove_exercise_muscle_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='exercisemachine',
            table='exercise_machine',
        ),
        migrations.AlterModelTable(
            name='exercisemuscle',
            table='exercise_muscle',
        ),
    ]
