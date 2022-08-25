from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.StackedInline): #agregar respuestas a las preguntas con StackInline
    model = Choice #Asigno el modelo de donde se va a desplegar 
    extra = 3 #Numero de respuestas por pregunta

class QuestionAdmin(admin.ModelAdmin): #en esta clase puedo poner funcionalidades al admin de django usando los atributos de nuestro modelo
    fields = ["question_text", "pub_date"] #defino el orden de los campos (atributos) del modelo a llenar
    inlines = [ChoiceInline] #agrego la clase que me permite agregar respuestas
    list_display = ["question_text", "pub_date"]
    list_filter = ["pub_date"] #agregue una seccion al Django admin de filtrar por fechas
    search_fields = ["question_text"] #agrego un buscador de preguntas al Django admin 

admin.site.register(Question, QuestionAdmin) #se agrega como parametro la clase QuestionAdmin
