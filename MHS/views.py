from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse('Hello, World!')


def about(request):
    return HttpResponse('Hello, About!')

def contact(request):
    return HttpResponse('Hello, Contact!')

def health_test(request):
    return HttpResponse('Hello, Test!')

def chatbot(request):
    return HttpResponse('Hello, Chatbot!')
