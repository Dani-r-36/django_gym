from django.test import TestCase
from .models import Machine 
# Create your tests here.

class MachineTestCase(TestCase):

    def test_machine_creation(self):
        machine = Machine.objects.create(ID = 1, name='Test Machine')
        self.assertEqual(str(machine), 'Test Machine')