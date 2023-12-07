from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # body
    return HttpResponse('wlcome')
def home(request):
    # body
    return HttpResponse('wlcome amir')
