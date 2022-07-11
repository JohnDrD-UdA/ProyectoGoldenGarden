from django.shortcuts import render

from .models import Tip
#from .forms import PosterForm
# Create your views here.

def tips(request):
    return render(request,'tips.html')

def inicio(request):
    tip = Tip.objects.all()
    contexto = {
        'tip' : tip
    }
    return render(request,'tips.html',contexto)

def mostrarPost(request,id):
    tip = Tip.objects.get(id = id)
    contexto = {
        'tip' : tip
    }
    return render(request,'post/tips.html', contexto)

def crearPost(request):
    if request.method == 'GET':
        form = PosterForm()
        contexto = {
            'form' : form,
            'get' : True
        }
    else:
        form = PosterForm(request.POST, request.FILES)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.usuario = request.user
            form2.save()
            return redirect('index')
        contexto = {
            'form' : form,
            'get' : False
        }
    return render(request,'post/create.html', contexto)

def editarPost(request,id):
    post = Poster.objects.get(id = id)
    if request.method == 'GET':
        form = PosterForm(instance = post)
        contexto = {
            'form' : form
        }
    else:
        form = PosterForm(request.POST, request.FILES, instance = post)
        contexto = {
            'form' : form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'post/edit.html', contexto)

def verify(request,id):
    post = Poster.objects.get(id = id)
    contexto = {
        'post' : post
    }
    return render(request, 'post/verify.html', contexto)

def eliminarPost(request,id):
    post = Poster.objects.get(id = id)
    post.delete()
    return redirect('index')