"""Estructuras2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from aplication.principal.views import about, indexController, createPostController, editPostController, verifyController, deletePostController, showPostController
from aplication.tips.views import crearTip, mostrarTip,tips


urlpatterns = [
    path('admon/', admin.site.urls),
    path('acerca_de_nosotros/', about, name = 'about'),
    path('', indexController, name = 'index'),
    path('mostrar/<int:id>', showPostController, name = 'index_post'),    
    path('crear_publicacion/', createPostController, name = 'create_post'),    
    path('editar_publicacion/<int:id>', editPostController, name = 'edit_post'),
    path('verificar_eliminar_post/<int:id>', verifyController, name = 'verify_post'),
    path('eliminar_post/<int:id>', deletePostController, name = 'delete_post'),
    path('accounts/', include('allauth.urls')),
    path('tips/', tips, name = 'tips'),
    path('crear_tip/', crearTip, name = 'create_tips'),
    path('leer/<int:id>', mostrarTip, name = 'publication_tips'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
