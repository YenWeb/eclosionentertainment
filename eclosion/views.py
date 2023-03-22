from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html',{"LIndex":Index.objects.all()})

def bande(request):
    return render(request,'bande.html')

def local(request):
    return render(request,'local.html')

def contact(request):
    return render(request,'contact.html')

def detail(request):
    return render(request,'detail.html',{"LFilm":Film.objects.all()})

def shop(request):
    return render(request,'shop.html')

def more(request):
    return render(request,'more.html')

def actus(request):
    return render(request,'actus.html')

def ProjectDeveloppement(request):
    return render(request,'ProjectDeveloppement.html')

def ProjectProduction(request):
    return render(request,'ProjectProduction.html')

def ProjectPostprod(request):
    return render(request,'ProjectPostprod.html')

def series(request):
    return render(request,'Cseries.html')

def docs(request):
    return render(request,'Cdocs.html',{"LFilm":Film.objects.all()})

def FLM(request):
    return render(request,'Cflm.html')

def FCM(request):
    return render(request,'Cfcm.html')

def reportages(request):
    return render(request,'Creportages.html')


