from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def argumentsView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return HttpResponse('<h2>Solo otra página</h2>')

def myHomeView(*args, **kwargs):
    return HttpResponse('<h2>Hola mundo desde DJango</h2>')
