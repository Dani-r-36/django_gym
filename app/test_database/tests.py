from django.test import TestCase
from .models import Machine, CurrentLift 
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