from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Cliente, Medidor, MarcaMedidor

class MedidorForm(ModelForm):
    class Meta:
        model = Medidor
        fields = ['marca', 'costoMedidor', 'origen', 'cliente', 'direccion', 'parroquia']