from django.urls import path
from .views import IndexPageView, obtenerFecha, menuView, mostrar, datosform_view, widget_view, libroform_view, listbook, registro_view, login_view, logout_view

from . import views
urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path('fecha/<name>', obtenerFecha, name='fecha'),
    path('menu/', menuView, name='menu'),
    path('es_palindromo/<str:palabra>/', views.verificar_palindromo, name='verificar_palindromo'),
    path('mostrar/', mostrar, name='mostrar'),
    path('listbook/', listbook, name='listbook'),
    path('datosform/', datosform_view, name='datos_form'),
    path('widgetform/', widget_view, name='widgetform'),
    path('inputbook/', libroform_view, name='libroform'),
    path('registro/', registro_view, name="registro"), 
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),

]

