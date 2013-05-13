from django.db import models

class Autore(models.Model):
  nome = models.CharField(max_length=50)
  cognome =models.CharField(max_length=50)
  def __unicode__(self):
      return u"%s %s" % (self.nome, self.cognome)
  class Meta:
        verbose_name_plural = "Autori"


class Genere(models.Model):
  descrizione = models.CharField(max_length=30)
  def __unicode__(self):
      return self.descrizione
  class Meta:
        verbose_name_plural = "Generi"

class Libro(models.Model):
  titolo = models.CharField(max_length=200)
  autore = models.ForeignKey(Autore)
  genere = models.ForeignKey(Genere)
  
  def __unicode__(self):
      return self.titolo
  class Meta:
        verbose_name_plural = "Libri"  