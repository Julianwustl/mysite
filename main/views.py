from django.shortcuts import render
from django.http import HttpResponse



def homepage(request):
    ab = 8
    return render(request, 'Home.html', context= None)


# Create your views here.
