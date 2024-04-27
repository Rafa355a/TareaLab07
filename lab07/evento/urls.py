from django.urls import path
from . import views

urlpatterns = [
    path('crear_evento/', views.crear_evento, name='crear_evento'),
    path('registrar_evento/', views.registrar_evento, name='registrar_evento'),
    path('lista_eventos/', views.lista_eventos, name='lista_eventos'),
    path('actualizar_evento/<int:evento_id>/', views.actualizar_evento, name='actualizar_evento'),
    path('actualizar_registro/<int:registro_id>/', views.actualizar_registro, name='actualizar_registro'),
    path('eliminar_evento/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
    path('eliminar_registro/<int:registro_id>/', views.eliminar_registro, name='eliminar_registro'),
]
