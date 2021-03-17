from django.forms import ModelForm
from .models import Profile, User, Equipment, Task, Tool, Consumable, Photo

from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('location', 'hourly_rate')

class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ('model', 'make', 'mfg_year', 'description', 'age', 'incrementer', 'cost')

class ToolForm(ModelForm):
    class Meta:
        model = Tool
        fields =('tool_name', 'description')

class ConsumableForm(ModelForm):
    class Meta:
        model = Consumable
        fields = ('name', 'description', 'part_number', 'source', 'cost')