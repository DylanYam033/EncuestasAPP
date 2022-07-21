from django.db import models

#Al hacer el mapeo Django nos pasa a tablas nuestras clases 

class Question(models.Model):
    #Atributos de nuestra clase, lo que en la base de datos seran las columnas 
    question_text = models.CharField(max_length=100) #se indica que el atributo sera un varchar en la base de datos
    pub_date = models.DateField("date published") #se indica que el atributo sera tipo date en la base de datos 

class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #se indica que este atributo es llave foranea, o sea la llave primaria de question
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0) #se indica que este atributo es de tipo int con valor 0 por defecto
    
