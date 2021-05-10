from django.shortcuts import render
import json
import os


def task(request):
    with open('tasks/newTask.json') as json_file:
        data = json.load(json_file)
    data["num"] = int(request.GET.get('num', default="-1"))

    return render(request, 'tasks/html/task1.html', data)
