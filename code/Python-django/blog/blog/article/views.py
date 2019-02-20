from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def article_list(request):
    return HttpResponse("Hello World!")
