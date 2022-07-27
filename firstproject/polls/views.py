from django.shortcuts import render
from django.http import HttpResponse

#Las views son el backend de nuestra app, las cuales van a estar ligadas a un template(front)
def index(request): #vista basada en funcion, las views pueden estar basadas en funciones o clases. 
    return HttpResponse("Hello world")

def detail(request, question_id):
    """details of every question"""
    return HttpResponse(f'Estás viendo la pregunta {question_id}')

def results(request, question_id):
    """details of every question result"""
    return HttpResponse(f'Estás viendo los resultados de la pregunta {question_id}')

def vote(request, question_id):
    """Functions for voting confirmation"""
    return HttpResponse(f'Estás votando a la pregunta {question_id}')
    
    
