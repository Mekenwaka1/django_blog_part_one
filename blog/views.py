from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime

def home_page(request):
    context = {
        'name': 'Meke',
        'current_time': datetime.now()
    }
    response = render(request, 'index.html', context)
    return HttpResponse(response)
