from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# Create your views here.



def price_info(request):
    tasks = Task.objects.all()
    return render(request, "main/price_info.html", {'title': "Цены на виды протезирования", "tasks": tasks})


def about(request):
    return render(request, "main/about.html")