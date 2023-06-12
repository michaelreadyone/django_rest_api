from django.urls import path
from . import views

urlpatterns = [
    path('var', views.VariableHandler),
]
