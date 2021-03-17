from django.shortcuts import render, redirect
from django.contrib.auth import login

# import forms
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, ProfileForm, EquipmentForm, ToolForm, ConsumableForm

# import models
from .models import User, Profile, Equipment, Task, Tool, Consumable, Maint_Record, Photo

# Create your views here.

# ==== Home =====
def home(request):
    return render(request, 'home.html')

# ==== Register =====
def register_user(request):
    if request.method == 'POST':
        signup_form = NewUserForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('garage')

    signup_form = NewUserForm()
    login_form = AuthenticationForm()
    context = {'signup_form': signup_form, 'login_form': login_form}
    return render(request, 'login.html', context)

# ==== Profile ====
def profile(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.save()
            return redirect('profile')

    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user_id=request.user.id)
    profile_form = ProfileForm()
    context = {'user': user, 'profile_form': profile_form, 'profile': profile}
    return render(request, 'profile/profile.html', context)

def profile_edit(request):
    profile = Profile.objects.get(user_id=request.user.id)
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        location = request.POST['location']
        hourly_rate = request.POST['hourly_rate']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']

        if User.objects.filter(username=username).exclude(id=request.user.id).exists():
            context={'error': 'Username is already taken', 'profile': profile}
            return render(request, 'profile/edit.html', context)
        else:
            if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                context={'error': 'Email is already taken', 'profile': profile}
                return render(request, 'profile/edit.html', context)
            else:
                user.last_name = last_name
                user.first_name = first_name
                user.email = email
                user.profile.location = location
                user.profile.hourly_rate = hourly_rate
                user.username = username
                user.save()
                return redirect('profile')

    profile_form = ProfileForm(instance=profile)
    user_form = NewUserForm(instance=user)
    context = {'profile_form': profile_form, 'user_form': user_form, 'user': user, 'profile': profile}
    return render(request, 'profile/edit.html', context)

def profile_delete(request):
    User.objects.get(id=request.user.id).delete()
    return redirect('home')


# ==== Garage ====
def garage(request):
    equipment = Equipment.objects.filter(user_id=request.user.id)
    context = {'equipment': equipment}
    return render(request, 'garage.html', context)

# ==== Equipment ====
def equipment_create(request):
    if request.method == 'POST':
        equipment_form = EquipmentForm(request.POST)
        if equipment_form.is_valid():
            equipment = equipment_form.save(commit=False)
            equipment.user = request.user
            equipment.save()
            return redirect('equipment_show', equipment_id=equipment.id)
        else:
            context = {'error': "Something has gone wrong.  Try Again."}
            return render(request, 'equipment/create.html', context)

    equipment_form = EquipmentForm()
    context = {'equipment_form': equipment_form}
    return render(request, 'equipment/create.html', context)

def equipment_show(request, equipment_id):
    equipment = Equipment.objects.get(id=equipment_id)
    equipment_form = EquipmentForm(instance=equipment)
    context = {'equipment': equipment, 'equipment_form': equipment_form}
    return render(request, 'equipment/show.html', context)

def equipment_edit(request, equipment_id):
    equipment = Equipment.objects.get(id=equipment_id)
    if request.method == 'POST':
        equipment_form = EquipmentForm(request.POST, instance=equipment)
        if equipment_form.is_valid():
            equipment_form.save()
            return redirect('equipment_show', equipment_id=equipment.id)

# ==== Tools ====
def tool_index(request):
    tool = Tool.objects.filter(user_id=request.user.id)
    context = {'tool': tool}
    return render(request, 'tools/index.html', context)

def tool_create(request):
    if request.method == 'POST':
        tool_form = ToolForm(request.POST)
        if tool_form.is_valid():
            tool = tool_form.save(commit=False)
            tool.user = request.user
            tool.save()
            return redirect('tool_index')
        else:
            return redirect('tool_index')

def tool_edit (request, tool_id):
    tool = Tool.objects.get(id=tool_id)
    if request.method == 'POST':
        tool_form = ToolForm(request.POST, instance=tool)
        if tool_form.is_valid():
            tool_form.save()
            return redirect('tool_index')

    tool_form = ToolForm(instance=tool)
    context = {'tool_form': tool_form, 'tool':tool}
    return render(request, 'tools/edit.html', context)

def tool_delete(reqeust, tool_id):
    Tool.objects.get(id=tool_id).delete()
    return redirect('tool_index')

# ==== Consumables ====
def consumable_index(request):
    consumable = Consumable.objects.filter(user_id=request.user.id)
    context = {'consumable': consumable}
    return render(request, 'consumables/index.html', context)

def consumable_create(request):
    if request.method == 'POST':
        consumable_form = ConsumableForm(request.POST)
        if consumable_form.is_valid():
            consumable = consumable_form.save(commit=False)
            consumable.user = request.user
            consumable.save()
            return redirect('consumable_index')
        else:
            return redirect('consumable_index')

def consumable_edit (request, consumable_id):
    consumable = Consumable.objects.get(id=consumable_id)
    if request.method == 'POST':
        consumable_form = ConsumableForm(request.POST, instance=consumable)
        if consumable_form.is_valid():
            consumable_form.save()
            return redirect('consumable_index')

    consumable_form = ConsumableForm(instance=consumable)
    context = {'consumable_form': consumable_form, 'consumable':consumable}
    return render(request, 'consumables/edit.html', context)

def consumable_delete(reqeust, consumable_id):
    Consumable.objects.get(id=consumable_id).delete()
    return redirect('consumable_index')