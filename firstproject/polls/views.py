from django.shortcuts import render
from django.http import HttpResponse

#importo el modelo de question 
from .models import Question

#Las views son el backend de nuestra app, las cuales van a estar ligadas a un template(front)
def index(request): #vista basada en funcion, las views pueden estar basadas en funciones o clases. 
    latest_question_list = Question.objects.all #objeto queryset (conjuntos) con las preguntas
    return render(request, "polls/index.html", { #render lleva tres parametros: request, ruta del template y un contexto(diccionario)
        "latest_question_list": latest_question_list #dejamos disponible la variable para ser usada en index.html
    })

def detail(request, question_id):
    """details of every question"""
    return HttpResponse(f'Estás viendo la pregunta {question_id}')

def results(request, question_id):
    """details of every question result"""
    return HttpResponse(f'Estás viendo los resultados de la pregunta {question_id}')

def vote(request, question_id):
    """Functions for voting confirmation"""
    return HttpResponse(f'Estás votando a la pregunta {question_id}')
    
    
