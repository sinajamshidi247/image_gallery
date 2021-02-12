from django.urls import path 
from .import views


app_name = 'photo'

urlpatterns = [
    path('',views.home,name='home'),
    path('<int:pk>/',views.detail,name='detail'),
    path('add/',views.addPhoto,name='add'),
]