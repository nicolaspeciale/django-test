from django.http import HttpResponse

def my_page(request):
  html="<html> <body> <p> Ciao Nicola </p> </body> </html>"
  return HttpResponse (html)
