from django.urls import path
from . import views

urlpatterns = [
    #se llaman las views creadas en views, las cuales son funciones
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="index"), 
    path("<int:question_id>/results/", views.results, name="index"),
    path("<int:question_id>/vote/", views.vote, name="index"),
]
