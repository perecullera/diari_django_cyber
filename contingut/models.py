# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify

import datetime
from django.utils.timezone import utc



class Noticia(models.Model):

  # relations

  # atributs
  titol = models.CharField(max_length=300)
  short_body = models.TextField(verbose_name = u"short body")
  body = models.TextField(verbose_name = u"body")
  created_at = models.DateTimeField(verbose_name = u"created at")
  published_at = models.DateTimeField(verbose_name = u"published at")
  visits = models.IntegerField(default = 0,
                               verbose_name = u"visits")


class Anunci(models.Model):
    #relations
    noticia = models.ForeignKey(u"Noticia",
                             related_name = u"anunci",
                             verbose_name = u"noticia")

    #atributs
    titol = models.CharField(max_length=300)
    cos = models.TextField()

class Sections(models.Model):
    #relations
    noticia = models.ForeignKey(u"Noticia",
                             related_name = u"section",
                             verbose_name = u"noticia")

    #atribituts
    titol = models.CharField(max_length=300)
