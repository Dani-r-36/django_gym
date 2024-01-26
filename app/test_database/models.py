from django.db import models


class Machine(models.Model):
    """Required fields for machine table"""
    ID = models.AutoField(primary_key=True, db_column='machine_id')
    name = models.CharField(max_length=50, db_column='machine_name')

    """links to metadata from table machine, which stores the data"""
    class Meta:
        db_table = 'machine'
        managed = False
    
    """returns just name of machine when model called"""
    def __str__(self):
        return self.name
    
    """creates a new machine instance called other, 
    where classmethod allows us to call method on the class instead of just for that instance"""
    @classmethod
    def get_other_option(cls):
        return cls(name='Other')

    """property deco allows us to access the attribute itself, where here we are checking if the name is other"""
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
    ID = models.AutoField(primary_key=True, db_column='muscle_id')
    name = models.CharField(max_length=70, db_column='muscle_name')
    group = models.ForeignKey(MuscleGroup,on_delete=models.CASCADE)

    class Meta:
        db_table = 'muscle'
    
    def __str__(self):
        return self.name
    
class ExerciseMuscle(models.Model):
    ID = models.AutoField(primary_key=True, db_column='exercise_muscle_id')
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)
    muscle = models.ForeignKey('Muscle', on_delete=models.CASCADE)

    class Meta:
        db_table = 'exercise_muscle'
        unique_together = ('exercise', 'muscle')
        managed = False

class ExerciseMachine(models.Model):
    ID = models.AutoField(primary_key=True, db_column='exercise_machine_id')
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)
    machine = models.ForeignKey('Machine', on_delete=models.CASCADE)

    class Meta:
        db_table = 'exercise_machine'
        unique_together = ('exercise', 'machine')

    
class CurrentLift(models.Model):
    ID = models.AutoField(primary_key=True, db_column='current_id')
    weight = models.FloatField(max_length=10, db_column='max_working_weight')
    reps = models.CharField(max_length=10, db_column='max_reps')
    # exercise_details = models.OneToOneField('ExerciseDetails', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'current_lift'

    def __str__(self):
        return f'{self.weight} : {self.reps}'

class Exercise(models.Model):
    ID = models.AutoField(primary_key=True, db_column='exercise_id')
    exercise_name = models.CharField(max_length=20, db_column='exercise_name')
    muscles = models.ManyToManyField(Muscle, through='ExerciseMuscle')
    machines = models.ManyToManyField(Machine, through='ExerciseMachine')
    # exercise_details = models.OneToOneField('ExerciseDetails', on_delete=models.CASCADE, null=True, blank=True, related_name='exercise_details')

    class Meta:
        db_table = 'exercise'

    def __str__(self):
        return self.exercise_name
    
    
class ExerciseDetails(models.Model):
    ID = models.AutoField(primary_key=True, db_column='exercise_details_id')
    exercise = models.ForeignKey("Exercise", on_delete=models.CASCADE)
    current = models.OneToOneField("CurrentLift", on_delete=models.CASCADE, null=True, blank=True)
    intensity = models.IntegerField( db_column='intensity')
    tips = models.CharField(max_length=200, db_column='tips')
    optimum = models.IntegerField(db_column='optimum_level')
    link = models.CharField(max_length=300, db_column='picture_video_link')
    
    class Meta:
        db_table = 'exercise_details'

    def __str__(self):
        return f'{self.intensity} : {self.tips} : {self.optimum} : {self.link}'