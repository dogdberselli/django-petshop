from datetime import date
from django import forms
from reserva.models import Reserva

class ReservaForm(forms.ModelForm):

    def clean_data(self):
        data = self.cleaned_data['data']
        hoje = date.today()
        reserva = Reserva.objects.filter(data=data).count()
        if data < hoje:
            raise forms.ValidationError('Não é possivel realizar uma reserva para o passado!')
        if reserva >= 4:
            raise forms.ValidationError('Não é possivel realizar mais reservas nesta data!')
        return data
    

    class Meta:
        model = Reserva
        fields = ['nome','email','nome_pet','data','turno','tamanho','observacoes']
