from django.urls import path
from . import views

app_name = 'Articles'
urlpatterns = [
	path('', views.index, name='index'),
]
