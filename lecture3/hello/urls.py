from os import path
from django.urls import path
from . import views

urlpatterns =[
    path ("", views.index, name="index"),
    path ("page", views.page, name="page"),
    path ("<str:name>", views.greet, name="greet"),
    path ("greetWorld/<str:name>", views.greetWorld, name="greetWorld"),
    path ("brian", views.brian, name="brian"),
]