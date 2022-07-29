from django.shortcuts import redirect,render
from .models import Tip
from .forms import TipForm
#from .forms import TipForm
# Create your views here.

def tips(request):
    tip = Tip.objects.all()
    contexto = {
        'tip' : tip
    }
    return render(request,'tips.html',contexto)

def mostrarTip(request,id):
    tip = Tip.objects.get(id = id)
    contexto = {
        'tip' : tip
    }
    return render(request,'tips/publication.html', contexto)

def crearTip(request):
    if request.method == 'GET':
        form = TipForm()
        contexto = {
            'form' : form,
            'get' : True
        }
    else:
        form = TipForm(request.POST, request.FILES)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.usuario = request.user
            form2.save()
            return redirect('tips')
        contexto = {
            'form' : form,
            'get' : False
        }
    return render(request,'tips/create.html', contexto)

def editarTip(request,id):
    tip = Tip.objects.get(id = id)
    if request.method == 'GET':
        form = TipForm(instance = tip)
        contexto = {
            'form' : form
        }
    else:
        form = TipForm(request.POST, request.FILES, instance = tip)
        contexto = {
            'form' : form
        }
        if form.is_valid():
            form.save()
            return redirect('tips')
    return render(request,'post/edit.html', contexto)

def verify(request,id):
    tip = Tip.objects.get(id = id)
    contexto = {
        'tip' : tip
    }
    return render(request, 'post/verify.html', contexto)

def eliminarTip(request,id):
    tip = Tip.objects.get(id = id)
    tip.delete()
    return redirect('tips')
