from django.shortcuts import render, redirect
from .services import libros, es_palindromo
from django.http import HttpResponseRedirect, HttpResponse
from tokenize import PseudoExtras
from django.views.generic import TemplateView
import datetime
from .forms import InputForm, WidgetForm, BoardsForm, RegistroUsuarioForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import BoardsModel
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.

class IndexPageView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    login_url = '/login/'
    permission_required = 'libro.es_miembro_1'
    template_name = "index.html"

def obtenerFecha(request, name):
 fechaActual = datetime.datetime.now()
 context = {'fecha' : fechaActual, 'name' : name}
 return render(request, 'fecha.html', context)

def menuView(request):
 template_name = 'menu.html'
 return render(request, template_name)

def listbook(request):
  context = {"libros": libros}
  return render(request, 'listbook.html', context)

def verificar_palindromo(request, palabra):
    if es_palindromo(palabra):
        mensaje = f"'{palabra}' es un palíndromo."
    else:
        mensaje = f"'{palabra}' no es un palíndromo."

    return HttpResponse(mensaje)

def navbar(request):
   
   return render(request, 'navbar.html', {})

def footer(request):
   
   return render(request, 'footer.html', {})

class Persona(object):
    def __init__ (self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido 

def mostrar(request):
 persona = Persona("Juan", "Peréz", True)
 items=["Primero", "Segundo", "Tercero", "Cuarto"]
 hrs= datetime.datetime.now()
 #items=[]
 context = {'nombre' : persona.nombre, "apellido" : persona.apellido, "login" : persona.login, "items" : items, "hora" : hrs}
 return render(request, "templatesexample.html", context)

def datosform_view(request):
    context = {}
    context['form']= InputForm()
    return render(request, "datosform.html", context)

def widget_view(request):
 context = {}
 form = WidgetForm(request.POST or None)
 context['form'] = form
 return render(request, "widget_home.html", context)

@login_required
def libroform_view(request):
    context ={}
 # crear el objeto form
    form = BoardsForm(request.POST or None, request.FILES or None)
 # verificar si el formulario es valido
    if form.is_valid():
 # guardar los datos del formulario al modelo
        form.save()
        return HttpResponseRedirect('/')
    context['form']= form
    return render(request, "libroform.html", context)

def registro_view(request):
 if request.method == "POST":
    form = RegistroUsuarioForm(request.POST)
    if form.is_valid():
            user = form.save()
            content_type = ContentType.objects.get_for_model(BoardsModel)

            es_miembro_1 = Permission.objects.get(
                codename='es_miembro_1',
                content_type=content_type
            )

            add_boards = Permission.objects.get(
                codename='add_boardsmodel',
                content_type=content_type
            )

            view_boards = Permission.objects.get(
                codename='view_boardsmodel',
                content_type=content_type
            )

 # Agregamos el permisos al usuario
            user.user_permissions.add(es_miembro_1, add_boards, view_boards)
            user.is_staff = True
            user.save()
            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente.")
            return HttpResponseRedirect ('/menu')
    messages.error(request, "Registro invalido. Algunos datos son incorrectos.")       
    form = RegistroUsuarioForm()
    return render (request= request,
template_name="registration/registro.html",
context={"register_form":form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}.")
                return HttpResponseRedirect('/menu')
            else:
                messages.error(request,"Invalido username o password.")
        else:
            messages.error(request,"Invalido username o password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form":form})

def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/menu')

@login_required
def libro_add(request):
    if request.method == 'POST':
        form = BoardsForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo libro en la base de datos
            messages.success(request, "Libro agregado exitosamente.")
            return redirect('listbook')  # Redirige a la lista de libros
        else:
            messages.error(request, "Error al agregar el libro. Por favor, verifica los datos.")
    else:
        form = BoardsForm()

    return render(request, 'libro_add.html', {'form': form})