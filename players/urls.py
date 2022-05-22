from django.urls import path

from . import views

urlpatterns = [
    path('', views.create_note, name='create_player'),
    path('delete', views.delete_player,name='delete') 
]