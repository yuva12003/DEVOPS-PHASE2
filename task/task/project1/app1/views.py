from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())
def about(request):
    template=loader.get_template('about.html')
    return HttpResponse(template.render())
def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())
def contact(request):
    template=loader.get_template('contact.html')
    return HttpResponse(template.render())
