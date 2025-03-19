from django.shortcuts import render
from .models import student

def task_list(request):
      tasks = student.objects.all()
      return render(request, 'task_list.html', {"tasks":tasks})