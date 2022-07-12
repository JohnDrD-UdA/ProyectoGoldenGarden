from django import  forms
from .models import Tip





class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['titulo', 'contenido', 'categoria', 'imagen']
        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Titulo'}),
            'contenido' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Contenido'}),
            'categoria' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Categoria'}),
        }