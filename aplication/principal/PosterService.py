from aplication.principal.forms import PosterForm
from .models import Poster

def getAllActivePosters():
    return Poster.objects.all()
def getPosterById(id):
    return Poster.objects.get(id=id)

def createNewPost(form,user):        
    if form.is_valid():
        form2 = form.save(commit=False)
        form2.usuario = user
        form2.save()
        return True
    else: return False

def editPoster(form):
    if form.is_valid():
            form.save()
            return True
    else: return False

def deletePost(id):
    post = Poster.objects.get(id = id) 
    post.delete()
    