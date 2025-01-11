from django.urls import path
from . import views

urlpatterns = [
    path('', views.sayHello, name='sayHello'),
    path('pornpics/',views.pornpics,name='pornpics'),
    path('xnxx/',views.xnxx,name='xnxx'),
    path('anal/',views.anal,name='anal'),
    path('porn/',views.porn,name='porn'),
]
