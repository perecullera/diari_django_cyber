# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from contingut.models import Noticia, Sections, Anunci

def index(request):
    latest_notice_list = Noticia.objects.order_by('-published_at')
    sections = Sections.objects.all()
    return render_to_response('index.html', {'latest_notice_list':latest_notice_list,
    								'sections':sections})
