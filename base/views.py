from django.shortcuts import render, redirect
from base.forms import ContatoForm, ReservaForm

#view de inicio
def inicio(request):
    return render(request, 'inicio.html')
    
#view do contato
def contato(request):
    sucesso = False
    if request.method == 'GET':
      form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
           sucesso = True
           form.save()

    contexto = {
       'telefone': '(99) 87382-3211',
       'responsavel': 'João da Silva',
       'form': form,
       'sucesso': sucesso
    }
    return render(request, 'contato.html', contexto)

#view de reserva
def reserva(request):
    sucesso = False
    if request.method == 'GET':
       form = ReservaForm()
    else:
        form = ReservaForm(request.POST)
        if form.is_valid():
            sucesso = True
            form.save()
    
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'reserva.html', contexto)
