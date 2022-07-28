from ast import Try
from audioop import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic #importo las views generic

#importo el modelo de question 
from .models import Question, Choice

class IndexView(generic.ListView): #vista basada en clases 
    #atributos de la clase
    template_name = "polls/index.html" #ruta del template
    context_object_name = "latest_question_list" 

    def get_queryset(self): #metodo de la clase IndexView
        """Return the last published questions"""
        return Question.objects.order_by("-pub_date")

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html" #ruta del template

class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html" #ruta del template


def vote(request, question_id): # recibe dos parametros que vienen de detail.html
    question =get_object_or_404(Question, pk=question_id) #recibe el modelo Question y la pk de la question
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"]) #viene de name=choice en detail.html
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/results.html", { #render lleva tres parametros: request, ruta del template y un contexto(diccionario)
        "question": question, "error_message": "No elegiste una respuesta" 
    })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,))) #cuando vota lo rederigimos a otra template


#Las views son el backend de nuestra app, las cuales van a estar ligadas a un template(front)
# def index(request): #vista basada en funcion, las views pueden estar basadas en funciones o clases. 
#     latest_question_list = Question.objects.all #objeto queryset (conjuntos) con las preguntas
#     return render(request, "polls/index.html", { #render lleva tres parametros: request, ruta del template y un contexto(diccionario)
#         "latest_question_list": latest_question_list #dejamos disponible la variable para ser usada en index.html
#     })

# def detail(request, question_id):
#     question = get_object_or_404 (Question, pk = question_id) #arroja el error 404
#     return render(request, "polls/detail.html", { #render lleva tres parametros: request, ruta del template y un contexto(diccionario)
#         "question": question #dejamos disponible la variable para ser usada en index.html
#     })
    

# def results(request, question_id):
#     question =get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", { #render lleva tres parametros: request, ruta del template y un contexto(diccionario)
#         "question": question 
#     })