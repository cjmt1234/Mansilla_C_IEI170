from django import forms
from Eva2_app.models import Reservas

class FormReservas(forms.ModelForm):

    
    class Meta:
        model = Reservas
        fields =  ['nombre', 'telefono', 'fechaReserva', 'hora', 'cantidad', 'correo', 'estado', 'observación']

        ESTADOS = [('reservado', 'RESERVADO'),('completada','COMPLETADA'), ('anulada','ANULADA'), ('no asisten','NO ASISTEN')]
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre','class':'form-control'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese el número teléfono ej:(9xxxxxxxx)', 'class':'form-control'}),
            'fechaReserva': forms.TextInput(attrs={'placeholder': 'Ingrese la fecha de reserva', 'class':'form-control', 'type':'date'}),
            'hora': forms.TextInput(attrs={'placeholder': 'Ingrese la hora de reserva', 'class':'form-control', 'type':'time'}),
            'cantidad': forms.NumberInput(attrs={'placeholder': 'Ingrese la cantidad de personas (entre 1 y 15)', 'class':'form-control'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Ingrese el correo electrónico', 'class':'form-control'}),
            'estado': forms.Select(choices=ESTADOS, attrs={'class':'form-select'}),
            'observación': forms.Textarea(attrs={'placeholder': 'Ingrese las observaciones', 'class':'form-control'}),
        }


    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']

        if not (1 <= cantidad <= 15):
            raise forms.ValidationError('La cantidad debe estar entre 1 y 15.')

        return cantidad
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']

        if len(nombre) > 80:
            raise forms.ValidationError('El nombre no debe tener más de 80 caracteres.')

        return nombre
    
    def clean_telefono(self):
        telefono= self.cleaned_data['telefono']

        if len(telefono) != 9 or int(telefono) >= 1000000000 or int(telefono) < 900000000:
            raise forms.ValidationError('El telefono no es válido.')

        return telefono
    

    