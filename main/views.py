# -*- coding: utf-8 -*-
from django.template import loader, Context, RequestContext, Template
from django.http import HttpResponse
from django.shortcuts import redirect
from models import *
from forms import *
from django.contrib.auth.decorators import login_required

def hello(request):
    page = Page.objects.get(name='main')
    t = loader.get_template("index.html")
    c = RequestContext(request, {'a': page})
    return HttpResponse(t.render(c))

def pages(request, str):
    page = Page.objects.get(name=str)
    t = loader.get_template("index.html")
    c = RequestContext(request, {'a': page})
    return HttpResponse(t.render(c))


@login_required
def main(request):
    if request.user.is_secretary or request.user.is_superuser:
        return show_table(request)
    else:
        return show_form(request)


@login_required
def show_form(request):
        account, created = Account.objects.get_or_create(user=request.user)
        form = AccountForm(instance=account)

        t = loader.get_template("form.html")
        c = RequestContext(request, {
            'account': form
        })
        return HttpResponse(t.render(c))


@login_required
def show_table(request):
    account = Account.objects.all()

    t = loader.get_template("accounts_list.html")
    c = RequestContext(request, {'account': account})
    return HttpResponse(t.render(c))


def save(request):
    if request.method == 'POST':
        account, created = Account.objects.get_or_create(user=request.user)
        account_form = AccountForm(request.POST, request.FILES, instance=account)
        if account_form.is_valid():
            account = account_form.save()

    return redirect('/')

def specialty(request, str):
    spec = Speciality.objects.filter(faculty=str)
    t = loader.get_template("specialty.html")
    c = RequestContext(request, { 'speciality': spec, })
    return HttpResponse(t.render(c))