

from django.contrib import admin
from django.urls import path

from .views import pagina_inicial, site

urlpatterns = [
    path('', pagina_inicial),

]
