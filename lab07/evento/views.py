from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventoForm
from .forms import RegistroEventoForm
from .models import Evento, RegistroEvento
from .forms import EventoForm, RegistroEventoForm

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'crear_evento.html', {'form': form})

def registrar_evento(request):
    if request.method == 'POST':
        form = RegistroEventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = RegistroEventoForm()
    return render(request, 'registrar_evento.html', {'form': form})

def lista_eventos(request):
    eventos = Evento.objects.all()
    registros = RegistroEvento.objects.all()
    return render(request, 'lista_eventos.html', {'eventos': eventos, 'registros': registros})

def actualizar_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'actualizar_evento.html', {'form': form})

def actualizar_registro(request, registro_id):
    registro = get_object_or_404(RegistroEvento, pk=registro_id)
    if request.method == 'POST':
        form = RegistroEventoForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = RegistroEventoForm(instance=registro)
    return render(request, 'actualizar_registro.html', {'form': form})

def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    evento.delete()
    return redirect('lista_eventos')

def eliminar_registro(request, registro_id):
    registro = get_object_or_404(RegistroEvento, pk=registro_id)
    registro.delete()
    return redirect('lista_eventos')

def home(request):
    return render(request, 'home.html')