# Generated by Django 4.2.7 on 2023-11-03 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
