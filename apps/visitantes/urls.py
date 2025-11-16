from django.urls import path, include
from . import views
from rest_framework import routers 

app_name = 'visitantes'

router = routers.DefaultRouter()
router.register('', views.VisitanteViewSet,
base_name= 'visitantes')

urlpatterns = [
    path('', include(router.urls))
]