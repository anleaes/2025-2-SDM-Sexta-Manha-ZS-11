from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'proprietarios'

router = routers.DefaultRouter()
router.register('', views.ProprietarioViewSet, basename='proprietarios')

urlpatterns = [
    path('', include(router.urls) )
]
