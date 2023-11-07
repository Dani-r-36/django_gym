from django.shortcuts import render, redirect

# Create your views here.
from .models import exercise, MuscleGroup
from .form import ExerciseForm, MuscleGroupForm

def index(request):
    data = exercise.objects.all()
    print(data)
    template_name = 'data.html'
    context = {"exercise":data}
    return render(request, template_name, context)

def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            # Create a new instance of the Exercise model
            new_exercise = exercise(Name=form.cleaned_data['Name'])
            new_exercise.save()
            return redirect('data.html')  # Redirect to a success page
    else:
        form = ExerciseForm()

    return render(request, 'add_exercise.html', {'form': form})

# def select_muscle_group(request):
#     muscle_groups = list(MuscleGroup.objects.values_list('ID', 'name'))

#     if request.method == 'POST':
#         form = MuscleGroupForm(request.POST)
#         if form.is_valid():
#             muscle_group = form.cleaned_data['muscle_group']
#             other_muscle_group = form.cleaned_data['other_muscle_group']
#             print("here other-",other_muscle_group)
#             print("here -",muscle_group)
#             if muscle_group and muscle_group != "Other":
#                 # User selected an existing muscle group
#                 # You can use muscle_group as needed
#                 print(muscle_group)
#                 pass
#             elif other_muscle_group:
#                 # User selected "Other" and provided a custom input
#                 # You can save the custom input or process it as needed
#                 # For example, create a new MuscleGroup
#                 # muscle_group = MuscleGroup.objects.create(name=other_muscle_group)
#                 print(muscle_group)
#             return redirect('data.html')
#         else:
#             print(form.errors)
#     else:
#         # Add the "Other" option to the choices
#         print("adding other")
#         muscle_groups.insert(0, (0, 'Other'))
#         form = MuscleGroupForm(initial={'muscle_group': 0})
#         form.fields['muscle_group'].choices = muscle_groups  # Update the choices
#         print(form.fields)
#         print(form.fields['muscle_group'])
#         print(form.fields['muscle_group'].choices)

#     return render(request, 'select_muscle_group.html', {'form': form})

def select_muscle_group(request):
    if request.method == 'POST':
        form = MuscleGroupForm(request.POST)
        if form.is_valid():
            muscle_group = form.cleaned_data['muscle_group']
            other_muscle_group = form.cleaned_data['other_muscle_group']
            print("here -",muscle_group)
            if muscle_group =="Other":
                # muscle_group = MuscleGroup.objects.create(name=other_muscle_group)
                print("Custom value entered: ", other_muscle_group)
            else:
                print("Selected muscle group: ", muscle_group)
            return redirect('data')
        else:
            print(form.errors)
    else:
        form = MuscleGroupForm()

    return render(request, 'select_muscle_group.html', {'form': form})



