from django import forms
from .models import exercise, MuscleGroup, Muscle, Machine

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = exercise
        fields = ['Name']  # Define the fields you want the user to input

class MuscleGroupForm(forms.Form):
    CHOICES = [
        ("", "Select a muscle group"),  # Empty value as the initial choice
    ]
    
    # Get the available muscle groups from the database
    muscle_groups = MuscleGroup.objects.values_list('ID', 'name')
    
    # Extend the choices list with the muscle groups from the database
    CHOICES.extend([(f"{str(id)}:{name}", name) for id, name in muscle_groups])
    
    # Add "Other" as a custom choice
    CHOICES.append(("Other", "Other"))
    
    choices = forms.ChoiceField(
        choices=CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'selectpicker'}),
    )
    other_choice = forms.CharField(max_length=50, required=False)



class MuscleForm(forms.Form):
    CHOICES = [
        ("", "Select a muscle"),  # Empty value as the initial choice
    ]
    # Get the available muscle groups from the database
    muscles = Muscle.objects.values_list('muscle_id', 'muscle_name')
    
    # Extend the choices list with the muscle groups from the database
    CHOICES.extend([(f"{str(id)}:{name}", name) for id, name in muscles])
    # # Add "Other" as a custom choice
    # CHOICES.append(("Other", "Other"))
    muscle = forms.ChoiceField(
        choices=CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'selectpicker'}),
    )

class MachineForm(forms.Form):
    CHOICES = [
        ("", "Select a muscle group"),  # Empty value as the initial choice
    ]
    
    # Get the available muscle groups from the database
    machines = Machine.objects.values_list('ID', 'name')
    
    # Extend the choices list with the muscle groups from the database
    CHOICES.extend([(f"{str(id)}:{name}", name) for id, name in machines])
    
    # Add "Other" as a custom choice
    CHOICES.append(("Other", "Other"))
    
    choices = forms.ChoiceField(
        choices=CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'selectpicker'}),
    )
    other_choice = forms.CharField(max_length=50, required=False)

