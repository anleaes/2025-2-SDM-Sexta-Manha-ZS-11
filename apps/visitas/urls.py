from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'visitas'

router = routers.DefaultRouter()
router.register('', views.VisitaViewSet, basename='visitas')

urlpatterns = [
    path('', include(router.urls) )
]
