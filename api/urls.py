from django.urls import path
from . import views

urlpatterns = [
    path("petshop/person",
         view=views.create_person, name="create_person")
]
