from django.shortcuts import render
from django.http import HttpResponse
#class based views
def home(request):
    return HttpResponse("Working fine!")
