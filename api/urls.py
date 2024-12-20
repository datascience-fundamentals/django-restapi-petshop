from django.urls import path
from . import views

urlpatterns = [
    path("petshop/person",
         view=views.person_view["persons_crd"], name="create_person"),
    path("petshop/person/<int:pk>",
         view=views.person_view["person_rud"], name="person_rud"),
    path("petshop/adoption-hist",
         view=views.adoption_view["adoption_hist"], name="adoption_hist"),
    path("petshop/breed",
         view=views.breed_view["breed_crud"].as_view({
             "get": "list",
             "post": "create",
         }), name="breeds_gp"),
    path("petshop/breed/<int:pk>",
         view=views.breed_view["breed_crud"].as_view({
             "get": "retrieve",
             "put": "update",
             "patch": "partial_update",
             "delete": "destroy",
         }), name="breed_rupd"),
    path("petshop/shelter",
         views.petshop_view["petshops_cr"].as_view(), name="petshops_cr"),
    path("petshop/shelter/<int:pk>",
         views.petshop_view["petshop_rud"].as_view(), name="petshop_rud"),
]
