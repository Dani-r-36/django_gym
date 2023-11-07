from django.db import models

# Create your models here.

class exercise(models.Model):
    ID = models.AutoField(primary_key=True, db_column='exercise_id')
    Name = models.CharField(max_length=20, db_column='exercise_name')

    class Meta:
        db_table = 'exercise'

    def __str__(self):
        return self.Name
    
class MuscleGroup(models.Model):
    ID = models.AutoField(primary_key=True, db_column='group_id')
    name = models.CharField(max_length=50, db_column='muscle_group')

    class Meta:
        db_table = 'group_muscle'
    
    def __str__(self):
        return self.name