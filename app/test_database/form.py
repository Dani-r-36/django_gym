from django import forms
from .models import Exercise, MuscleGroup, Muscle, Machine, ExerciseDetails, CurrentLift

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['exercise_name'] 

class MachineForm(forms.Form):
    CHOICES = [
        ("", "Select a muscle group"),  # Empty value as the initial choice
    ]
    
    # # Get the available muscle groups from the database
    machines = Machine.objects.values_list('ID', 'name')
    
    # # Extend the choices list with the muscle groups from the database
    CHOICES.extend([(f"{str(id)}:{name}", name) for id, name in machines])
    
    # # Add "Other" as a custom choice
    CHOICES.append(("0:Other", "Other"))

    # CHOICES = [
    # ("", "Select a muscle group"),
    # *((id, name) for id, name in machines),  # Directly use ID as a number
    # (26, "Other"),  # Separate choice for "Other"
# ]
    
    machines = forms.MultipleChoiceField(
        choices=CHOICES,
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'selectpicker'}),
    )
    other_choice = forms.CharField(max_length=50, required=False)



class MuscleGroupForm(forms.Form):
    CHOICES = [
        ("", "Select a muscle group"),  # Empty value as the initial choice
    ]
    
    # Get the available muscle groups from the database
    muscle_groups = MuscleGroup.objects.values_list('ID', 'name')
    
    # Extend the choices list with the muscle groups from the database
    CHOICES.extend([(f"{str(id)}:{name}", name) for id, name in muscle_groups])
    
    
    muscle_group = forms.ChoiceField(
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
    muscles = Muscle.objects.values_list('ID', 'name')
    
    # Extend the choices list with the muscle groups from the database
    CHOICES.extend([(f"{str(id)}:{name}", name) for id, name in muscles])
    # # Add "Other" as a custom choice
    # CHOICES.append(("Other", "Other"))
    muscle = forms.MultipleChoiceField(
        choices=CHOICES,
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'selectpicker'}),
    )

class ExerciseDetailsForm(forms.ModelForm):
    class Meta:
        model = ExerciseDetails
        fields = ['intensity', 'tips','optimum', 'link'] 
        widgets = {
            'intensity': forms.TextInput(attrs={'placeholder': '0 is not intense and 3 is intense'}),
            'optimum': forms.TextInput(attrs={'placeholder': '0 is not optimum and 3 is optimum'}),
        }

class CurrentLiftForm(forms.ModelForm):
    class Meta:
        model = CurrentLift
        fields = ['weight', 'reps'] 