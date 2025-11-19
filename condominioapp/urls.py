"""
URL configuration for condominioapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('condominios/', include('condominios.urls', namespace='condominios') ),
    path('visitantes/', include('visitantes.urls', namespace='visitantes')),
    path('blocos/', include('blocos.urls', namespace='blocos')),
    path('funcionarios/', include('funcionarios.urls', namespace='funcionarios')),
    path('proprietarios/', include('proprietarios.urls', namespace='proprietarios')),
    path('apartamentos/', include('apartamentos.urls', namespace='apartamentos')),
    path('garagens/', include('garagens.urls', namespace='garagens')),
]
