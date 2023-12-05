from django.shortcuts import get_object_or_404, render, redirect
from Eva2_app.forms import FormReservas

from Eva2_app.models import Reservas


#Mis vistas

#Vista del menú principal
def index(request):
    return render(request, 'index.html')


#Vista del listado de Reservas
def lista(request):
    
    reserva = Reservas.objects.all()
    return render(request, 'lista.html', {'reserva':reserva})

#Vista para agregar datos
def agregar(request):
    if request.method == 'POST':
        form = FormReservas(request.POST)
        if form.is_valid():
           
            form.save()
            return render(request, 'exitoso.html')
    else:
        form = FormReservas()
    return render(request, 'agregar.html', {'form':form})


#Vista para editar datos

def editar(request, id):

    reserva = get_object_or_404(Reservas, pk=id)

    if request.method == 'POST':
        form = FormReservas(request.POST)
        if form.is_valid():
            form = FormReservas(request.POST, instance=reserva)
            form.save()
            return render(request, 'exitoso.html')
    else:
        form = FormReservas(instance=reserva)
    return render(request, 'editar.html', {'form':form})





#Vista para eliminar datos
def estasSeguro(request, id):
    reserva = Reservas.objects.get(pk=id)
    return render(request, "estasSeguro.html" ,{ 'reserva':reserva})

def eliminar(request, id):
    try:
            
        reserva = Reservas.objects.get(pk=id)

        reserva.delete()

        return render(request, 'exitoso.html')
    except:
        return redirect('Lista')




