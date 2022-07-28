from unicodedata import name
from django.urls import path
from . import views

app_name = "polls" #nombre de la app para referenciar los archivos
urlpatterns = [
    #se llaman las views creadas en views, las cuales son funciones
    path("", views.IndexView.as_view(), name="index"), #cuando son views basadas en clases se pone el nombre de la view y el .as_view()
    path("<int:pk>/detail/nea/wow", views.DetailView.as_view(), name="detail"), 
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"), 
    #con el name y el app name vamos a referenciar conectar el template con la views por medio del metodo de url
]
