# -*- coding: utf-8 -*-
from django.template import loader, Context, RequestContext, Template
from django.http import HttpResponse

def hello(request):
    t = loader.get_template("main.html")
    var = 1
    c = RequestContext(request, {'var': var})
    return HttpResponse(t.render(c))