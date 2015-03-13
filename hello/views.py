from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import requests
import os
# Create your views here.

def index(request):
    times = int(os.environ.get('TIMES', 3))
    r = requests.get('http://httpbin.org/status/418')
    return HttpResponse('<pre>' + r.text + '</pre>' + 'hello! ' * times)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

