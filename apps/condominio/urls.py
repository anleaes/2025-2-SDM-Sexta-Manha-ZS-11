from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'condominio'

router = routers.DefaultRouter()
router.register('', views.CondominioViewSet, basename='condominios')

urlpatterns = [
    path('', include(router.urls) )
]