from django.shortcuts import render
from django.http import HttpResponse
from .models import Task, About
# Create your views here.



def price_info(request):
    tasks = Task.objects.all()
    return render(request, "main/price_info.html", {'title': "Цены на виды протезирования", "tasks": tasks,})


def about(request):
    tasks = About.objects.all()
    return render(request, "main/about.html",  {'title': "Приветствие", "tasks": tasks})