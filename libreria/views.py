# Create your views here.
from django.http import HttpResponse
from models import *
from django.shortcuts import render_to_response

def libri(request):
    return render_to_response('libri.html', {'libri': Libro.objects.all().order_by ('titolo')})

    return HttpResponse(elenco)  

def libro(request, id):
    try:
        libro = Libro.objects.get(pk=id)
        return HttpResponse("'%s' di %s, %s<br>" % (libro.titolo, libro.autore , libro.genere))
    except Libro.DoesNotExist:
        return HttpResponse("Codice %s inesistente" % id)    