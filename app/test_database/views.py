from django.shortcuts import render, redirect

# Create your views here.
from .models import Exercise, MuscleGroup, Muscle, Machine
from .form import ExerciseForm, MuscleGroupForm, MuscleForm, MachineForm

def index(request):
    data = Exercise.objects.all()
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
    groups = MuscleGroup.objects.all()
    muscle_data = Muscle.objects.all()
    grouped_muscles = {}
    for group in groups:
        group_muscles = muscle_data.filter(group=group)
        grouped_muscles[group] = group_muscles

    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        machine_form = MachineForm(request.POST)
        muscle_form = MuscleForm(request.POST)
        if form.is_valid() and machine_form.is_valid() and muscle_form.is_valid():
            machine = machine_form.cleaned_data['machines']
            other_machine = machine_form.cleaned_data['other_choice']
            exercise = form.cleaned_data['exercise_name']
            muscle = muscle_form.cleaned_data['muscle']
            print(f"machine {machine},other machine {other_machine},exercsie{exercise}, muscle{muscle}")
            machine_ids = [int(select_machine.split(':')[0]) for select_machine in machine]
            muscle_ids = [int(select_muscles.split(':')[0]) for select_muscles in muscle]
            print(machine_ids, muscle_ids)
            new_exercise = Exercise.objects.create(exercise_name=exercise, machine=machine_ids, muscle=muscle_ids)
            print("hsdfsdfsdfdaef")
            # new_exercise.muscles.set(muscle_ids)
            # new_exercise.machines.set(machine_ids)
            new_exercise.save()
            return redirect('data.html')  # Redirect to a success page
    else:
        form = ExerciseForm()
        machine_form = MachineForm()
        muscle_form = MuscleForm()
    context = {'form': form, 'machine_form':machine_form, 'muscle_form':muscle_form, 'grouped_muscles': grouped_muscles}
    return render(request, 'form.html', context)




