from django.urls import path
from . import views

urlpatterns = [

	path('create/', views.create, name = 'create'),
	path('add/', views.add, name = 'add'),
	path('result', views.result, name = 'result'),
	path('first-class', views.show, name= 'first-class'),
	path('delete/<int:id>/', views.delete, name = 'delete'),


]