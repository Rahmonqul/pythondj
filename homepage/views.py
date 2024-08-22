from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class Hompageview(TemplateView):
    template_name = 'home.html'

class Aboutpageview(TemplateView):
    template_name = 'about.html'

class Loginpageview(TemplateView):
    template_name = 'login.html'

# Create your views here.

def homepage(request):
    return HttpResponse("hello world")