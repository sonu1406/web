from django.shortcuts import render
from .models import Job
from django.http import HttpResponse

def home(request):
    jobs=Job.objects
    return render(request,'./jobs/home.html', {"jobs":jobs})
