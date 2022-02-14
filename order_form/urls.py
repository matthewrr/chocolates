from django.urls import path 
from . import views

urlpatterns = [
	path('', views.wholesale_form, name='wholesale_form'),
	path('upload/', views.image_upload_view)
]