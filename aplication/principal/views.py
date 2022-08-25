from django.shortcuts import redirect, render

from aplication.principal.PosterService import *

from .models import Poster
from .forms import PosterForm
# Create your views here.

def about(request):
    return render(request,'about.html')


def indexController(request):
    poster = getAllActivePosters()
    contexto = {
        'poster' : poster
    }
    return render(request,'index.html',contexto)

def showPostController(request,id):
    poster = getPosterById(id)
    contexto = {
        'poster' : poster
    }
    return render(request,'post/index.html', contexto)

def createPostGetTypeRequest(request):
    form = PosterForm()
    contexto = {
            'form' : form,
            'get' : True
        }
    return render(request,'post/create.html', contexto)

def createPostPostTypeRequest(request):
    form = PosterForm(request.POST, request.FILES)
    response=createNewPost(form,request.user)         
    if response:
        return redirect('index')
    else:
        contexto = {
        'form' : form,
        'get' : False
        }     
        return render(request,'post/create.html', contexto)

def createPostController(request):
    if request.method == 'GET':
       return createPostGetTypeRequest(request)
    else:
       return  createPostPostTypeRequest(request)
def editPostGetTypeRequest(request,post):
    form = PosterForm(instance = post)
    contexto = {
            'form' : form
        }
    return render(request,'post/edit.html', contexto)

def editPostPostTypeRequest(request,post):
    form = PosterForm(request.POST, request.FILES, instance = post)
    response=editPoster(form)
    if(response):
        return redirect('index')
    else:
        contexto = {
            'form' : form
            }
        return render(request,'post/edit.html', contexto)

def editPostController(request,id):
    post = getPosterById(id)
    if request.method == 'GET':
       return editPostGetTypeRequest(request,post)
    else:
      return  editPostPostTypeRequest(request,post)
    

def verifyController(request,id):
    post = getPosterById(id)
    contexto = {
        'post' : post
    }
    return render(request, 'post/verify.html', contexto)

def deletePostController(request,id):
    deletePost(id)
    return redirect('index')

def myPostsController(request,id):
    poster = getPostByUser(id)
    contexto = {
        'poster' : poster
    }
    return render(request,'post/list.html',contexto)

