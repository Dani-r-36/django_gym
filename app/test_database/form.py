from django import forms
from .models import Exercise, MuscleGroup, Muscle, Machine

# class ExerciseForm(forms.ModelForm):
#     custom_machine_name = forms.CharField(max_length=50, required=False)
#     class Meta:
#         model = exercise
#         fields = ['exercise_name', 'machine', 'muscle']  # Define the fields you want the user to input
#     def clean(self):
#         cleaned_data = super().clean()
#         machine = cleaned_data.get('machine')
#         custom_machine_name = cleaned_data.get('custom_machine_name')

#         if machine.is_other_option and not custom_machine_name:
#             raise forms.ValidationError("Custom machine name is required when choosing 'Other'.")

#         return cleaned_data

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['exercise_name'] 


class MachineForm(forms.Form):
    CHOICES = [
        ("", "Select a muscle group"),  # Empty value as the initial choice
    ]
    
    # Get the available muscle groups from the database
    machines = Machine.objects.values_list('ID', 'name')
    
    # Extend the choices list with the muscle groups from the database
    CHOICES.extend([(f"{str(id)}:{name}", name) for id, name in machines])
    
    # Add "Other" as a custom choice
    CHOICES.append(("0:Other", "Other"))
    
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

# class MuscleForm(forms.Form):
#     muscle_group = forms.ChoiceField(
#         choices=[("", "Select a muscle group")],
#         required=False,
#         widget=forms.Select(attrs={'class': 'selectpicker'}),
#     )

#     muscle = forms.MultipleChoiceField(
#         choices=[("", "Select a muscle")],
#         required=False,
#         widget=forms.SelectMultiple(attrs={'class': 'selectpicker'}),
#     )