

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def pagina_inicial(request):
  return render(request, 'index.html')


def site(request):
  return HttpResponse("<b>viva a paz</b>")