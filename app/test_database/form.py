from django import forms
from .models import exercise,MuscleGroup

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = exercise
        fields = ['Name']  # Define the fields you want the user to input


# class MuscleGroupForm(forms.Form):
#     muscle_group = forms.ModelChoiceField(
#         queryset=MuscleGroup.objects.all(),
#         empty_label="Select a muscle group",
#         required=False,
#         widget=forms.Select(attrs={'class': 'selectpicker'}),  # Add a custom class if needed
#     )
#     other_muscle_group = forms.CharField(max_length=50, required=False)

#     def __init__(self, *args, **kwargs):
#         super(MuscleGroupForm, self).__init__(*args, **kwargs)
#         self.fields['muscle_group'].choices = [("", 'Other')] + list(self.fields['muscle_group'].choices)

class MuscleGroupForm(forms.Form):
    CHOICES = [
        ("", "Select a muscle group"),  # Empty value as the initial choice
    ]
    
    # Get the available muscle groups from the database
    muscle_groups = MuscleGroup.objects.values_list('ID', 'name')
    
    # Extend the choices list with the muscle groups from the database
    CHOICES.extend([(str(id), name) for id, name in muscle_groups])
    
    # Add "Other" as a custom choice
    CHOICES.append(("Other", "Other"))
    
    muscle_group = forms.ChoiceField(
        choices=CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'selectpicker'}),
    )
    other_muscle_group = forms.CharField(max_length=50, required=False)





