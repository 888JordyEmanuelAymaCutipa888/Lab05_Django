from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(*args, **kwargs):
    return HttpResponse('<h2>Hola mundo desde DJango</h2>')
