# Generated by Django 4.2.7 on 2023-11-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_database', '0002_alter_exercise_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='ID',
            field=models.IntegerField(db_column='ID', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='Name',
            field=models.CharField(db_column='exercise_name', max_length=20),
        ),
    ]
