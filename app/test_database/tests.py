from django.test import TestCase
from .models import Machine, CurrentLift, Exercise, ExerciseDetails
# Create your tests here.

class MachineTestCase(TestCase):

    def test_machine_creation(self):
        machine = Machine.objects.create(ID = 1, name='Test Machine')
        self.assertEqual(str(machine), 'Test Machine')
    
    def test_get_other_option(self):
        other_machine = Machine.get_other_option()
        self.assertEqual(other_machine.name, 'Other')

    def test_is_other_option_property(self):
        other_machine = Machine.objects.create(name='Other')
        self.assertTrue(other_machine.is_other_option)

        regular_machine = Machine.objects.create(name='Regular Machine')
        self.assertFalse(regular_machine.is_other_option)

class CurrentTestCase(TestCase):

    def test_current_creation(self):
        current = CurrentLift.objects.create(ID = 1, weight=50, reps = "F7")
        self.assertEqual(str(current), '50 : F7')

class ExerciseTestCase(TestCase):

    def test_exercise_creation(self):
        exercise = Exercise.objects.create(ID = 1, exercise_name = "Fake exercise")
        self.assertEqual(str(exercise), "Fake exercise")

class ExerciseDetailsTestCase(TestCase):

    def test_exercise_creation(self):
        exercise_instance = Exercise.objects.create(ID = 1, exercise_name = "Fake exercise")
        current_instance = CurrentLift.objects.create(ID = 1, weight=50, reps = "F7")
        exercise_details = ExerciseDetails.objects.create(ID = 1, exercise = exercise_instance, current = current_instance, intensity = 2, tips = "Tip", optimum = 2, link = "link")
        self.assertEqual(str(exercise_details), "2 : Tip : 2 : link")
    
    def test_exercise_fail_creation(self):
        exercise_instance = Exercise.objects.create(ID = 1, exercise_name = "Fake exercise")
        current_instance = CurrentLift.objects.create(ID = 1, weight=50, reps = "F7")
        with self.assertRaises(ValueError) as context:
            exercise_details = ExerciseDetails.objects.create(
                ID=1,
                exercise=exercise_instance,
                current=current_instance,
                intensity="hello",
                tips="Tip",
                optimum=2,
                link="link"
            )
        
        self.assertIn("Field 'intensity' expected a number but got 'hello'", str(context.exception))