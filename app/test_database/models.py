from django.db import models

# Create your models here.


class Machine(models.Model):
    ID = models.AutoField(primary_key=True, db_column='machine_id')
    name = models.CharField(max_length=50, db_column='machine_name')

    class Meta:
        db_table = 'machine'
    
    def __str__(self):
        return self.name
    
    @classmethod
    def get_other_option(cls):
        return cls(name='Other')

    @property
    def is_other_option(self):
        return self.name == 'Other'

class MuscleGroup(models.Model):
    ID = models.AutoField(primary_key=True, db_column='group_id')
    name = models.CharField(max_length=50, db_column='muscle_group')

    class Meta:
        db_table = 'group_muscle'
    
    def __str__(self):
        return self.name
    

class Muscle(models.Model):
    muscle_id = models.AutoField(primary_key=True, db_column='muscle_id')
    muscle_name = models.CharField(max_length=70, db_column='muscle_name')
    group = models.ForeignKey(MuscleGroup,on_delete=models.CASCADE)

    class Meta:
        db_table = 'muscle'
    
    def __str__(self):
        return self.muscle_name

class Exercise(models.Model):
    ID = models.AutoField(primary_key=True, db_column='exercise_id')
    exercise_name = models.CharField(max_length=20, db_column='exercise_name')
    machine = models.ManyToManyField(Machine)
    muscle = models.ManyToManyField(Muscle)
    
    class Meta:
        db_table = 'exercise'

    def __str__(self):
        return self.exercise_name