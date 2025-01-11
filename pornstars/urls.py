
from django.urls import path
from . import views


urlpatterns = [
    path('', views.pornstars, name='index'),
    path('add/', views.add, name='add'),
    path('slide/',views.slide,name='slide')
]
