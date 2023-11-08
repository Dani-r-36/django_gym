from django.shortcuts import render, redirect

# Create your views here.
from .models import exercise, MuscleGroup, Muscle, Machine
from .form import ExerciseForm, MuscleGroupForm, MuscleForm, MachineForm

def index(request):
    data = exercise.objects.all()
    print(data)
    template_name = 'data.html'
    context = {"exercise":data}
    return render(request, template_name, context)

def select_muscle_group(request):
    if request.method == 'POST':
        form = MuscleGroupForm(request.POST)
        if form.is_valid():
            muscle_group = form.cleaned_data['choices']
            other_muscle_group = form.cleaned_data['other_choice']
            print(form.cleaned_data)
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

def select_muscle(request):
    if request.method == 'POST':
        form = MuscleForm(request.POST)
        if form.is_valid():
            muscle = form.cleaned_data['muscle']
            muscle_id, muscle_name = muscle.split(":")
            print(form.cleaned_data)
            print(f"here -{muscle_name}-{muscle_id}")
            return redirect('data')
        else:
            print(form.errors)
    else:
        form = MuscleForm()

    return render(request, 'form.html', {'form': form})

def select_machine(request):
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            machine = form.cleaned_data['choices']
            other_machine = form.cleaned_data['other_choice']
            print(form.cleaned_data)
            print("here -",machine)
            if machine =="Other":
                # muscle_group = MachineForm.objects.create(name=other_muscle_group)
                print("Custom value entered: ", other_machine)
            else:
                print("Selected muscle group: ", machine)
            return redirect('data')
        else:
            print(form.errors)
    else:
        form = MachineForm()

    return render(request, 'select_muscle_group.html', {'form': form})


# def add_exercise(request):
#     if request.method == 'POST':
#         form = ExerciseForm(request.POST)
#         if form.is_valid():
#             # Create a new instance of the Exercise model
#             new_exercise = exercise(Name=form.cleaned_data['Name'])
#             new_exercise.save()
#             return redirect('data.html')  # Redirect to a success page
#     else:
#         form = ExerciseForm()

#     return render(request, 'add_exercise.html', {'form': form})

def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        group = MuscleGroupForm(request.POST)
        machine_form = MachineForm(request.POST)
        muscle_form = MuscleForm(request.POST)
        if form.is_valid() and machine_form.is_valid() and muscle_form.is_valid():
            machine = machine_form.cleaned_data['machines']
            other_machine = machine_form.cleaned_data['other_choice']
            exercise = form.cleaned_data['exercise_name']
            muscle = muscle_form.cleaned_data['muscle']
            print(f"machine {machine},other machine {other_machine},exercsie{exercise}, muscle{muscle}")

            return redirect('data.html')  # Redirect to a success page
    else:
        form = ExerciseForm()
        machine_form = MachineForm()
        muscle_form = MuscleForm()

    return render(request, 'form.html', {'form': form, 'machine_form':machine_form, 'muscle_form':muscle_form})




def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        group_form = MuscleGroupForm(request.POST)
        if form.is_valid() and group_form.is_valid():
            muscle_group = group_form.cleaned_data['muscle_group']
            exercise = form.cleaned_data['exercise_name']
            print(f"muscle_group {muscle_group},exercsie{exercise}")

            return redirect('data.html')  # Redirect to a success page
    else:
        form = ExerciseForm()
        group_form = MuscleGroupForm()

    return render(request, 'form.html', {'form': form, 'group_form':group_form})

