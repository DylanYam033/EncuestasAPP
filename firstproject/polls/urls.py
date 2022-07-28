from unicodedata import name
from django.urls import path
from . import views

app_name = "polls" #nombre de la app para referenciar los archivos
urlpatterns = [
    #se llaman las views creadas en views, las cuales son funciones
    path("", views.index, name="index"),
    path("<int:question_id>/detail/nea/wow", views.detail, name="detail"), 
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"), 
    #con el nmame y el app name vamos a referenciar conectar el template con la views por medio del metodo de url
]
