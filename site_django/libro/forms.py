from django import forms
from .models import Book

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class InputForm(forms.Form):
 nombres = forms.CharField(max_length = 200)
 apellidos = forms.CharField(max_length = 200)
 prioridad = forms.IntegerField(min_value=1, max_value=3)
 contrasenna = forms.CharField(widget = forms.PasswordInput())

class WidgetForm(forms.Form):
 nombre = forms.CharField(widget = forms.Textarea)
 apellido = forms.CharField(widget = forms.CheckboxInput)
 prioridad = forms.IntegerField(widget = forms.TextInput)
 habilitado = forms.BooleanField(widget = forms.Textarea)
 date = forms.DateField(widget = forms.SelectDateWidget)

class BoardsForm(forms.ModelForm):
 # specify the name of model to use
 class Meta:
    model = Book
    fields = "__all__"

# Agregado para el registro de usuarios
class RegistroUsuarioForm(UserCreationForm):
 email = forms.EmailField(required=True)
 class Meta:
   model = User
   fields = ("username", "email", "password1", "password2")

 def save(self, commit=True):
   user = super(RegistroUsuarioForm, self).save(commit=False)
   user.email = self.cleaned_data['email']
   if commit:
     user.save()
   return user