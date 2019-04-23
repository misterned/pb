from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello PB')

def user_detail(request, name):
    body = "Nom : {}".format(name)
    return HttpResponse(body)
