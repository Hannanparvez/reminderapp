from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<slug:un>',views.home,name='home'),
]