from django.urls import path
from . import views

urlpatterns = [
    path("petshop/person",
         view=views.person_view["persons_crd"], name="create_person"),
    path("petshop/person/<int:pk>",
         view=views.person_view["person_rud"], name="person_rud"),
    path("petshop/adoption-hist",
         view=views.adoption_view["adoption_hist"], name="adoption_hist")
]
