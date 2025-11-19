from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'garagens'

router = routers.DefaultRouter()
router.register('', views.GaragemViewSet, basename='garagens')

urlpatterns = [
    path('', include(router.urls) )
]