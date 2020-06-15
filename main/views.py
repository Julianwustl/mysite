from django.shortcuts import render
from django.http import HttpResponse
import main.models as models



def homepage(request):
    ab = 8
    projects = models.project.object.get.all()
    return render(request, 'Home.html', context= None)


# Create your views here.
