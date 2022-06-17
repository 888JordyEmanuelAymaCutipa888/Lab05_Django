from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def usoContexto(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    myContext = {
            'myText': 'mi texto',
            'myNumber': 76,
            }
    return render(request, 'usoContexto.html', myContext)


def usoPlantilla(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'usoPlantilla.html', {})

def plantilla(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'home.html', {})

def argumentsView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return HttpResponse('<h2>Solo otra página</h2>')

def myHomeView(*args, **kwargs):
    return HttpResponse('<h2>Hola mundo desde DJango</h2>')
