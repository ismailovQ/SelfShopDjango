from django.urls import path

from apps.views import index, register_page

urlpatterns = [
	path('', index, name='index'),
	path('register', register_page, name='register')
]

