from django.shortcuts import render
from django.views.generic import TemplateView


def index(request, *args, **kwargs):
	return render(request, 'apps/auth/register-page.html')


def register_page(request, *args, **kwargs):
	return render(request, 'apps/auth/register-page.html')







