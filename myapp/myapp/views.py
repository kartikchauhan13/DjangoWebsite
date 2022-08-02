from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
    #return HttpResponse("<h1>this is index</h1>")
    isActive=True
    name='jerry'
    favFoods=['icecream','dry fishfood snacks','chicken gravy']
    data={
        'name':name,
        'foods':favFoods,
        'toys':{
            'wood':'ball',
            'rubber':'stick',
            'cotton':'teddy',
        }

    }

    return render(request,'home.html',data)

def about(request):
    #return HttpResponse("<h1>this is about page</h1>")
    return render(request,'about.html',{})

def services(request):
    #return HttpResponse("<h1>this is service page</h1>")
    return render(request,'services.html',{})