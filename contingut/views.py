# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from contingut import models


def index(request):
    sections = models.Noticia.objects.all()
    outstanding_noticies = models.Sections.objects.all().order_by("-id")[0:3]
    return render_to_response("index.html",
                              RequestContext(request,
                                             {
                                                 'sections': sections,
                                                 'outstanding_noticies': outstanding_noticies
                                                 }
                                             )
                              )
