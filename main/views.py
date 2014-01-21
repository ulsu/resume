# -*- coding: utf-8 -*-
from django.template import loader, Context, RequestContext, Template
from django.http import HttpResponse
from django.shortcuts import redirect
from models import *
from forms import *
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from resume import settings
from datetime import datetime
from django.db.models import Q



def mediaserver(request, path):
    return serve(request, path, settings.MEDIA_ROOT)

def search(request, year):
    if request.method == 'POST':
        if request.POST['search_query'] != '':
            query = request.POST['search_query'].split(' ')
            f = False
            for q in query:
                if len(q) >= 3:
                    f = True
                    break

            account = []
            if f:
                generic_query = Q(speciality__year=year)
                for q in query:
                    if len(q) >= 3:
                        generic_query &= (
                            Q(last_name__icontains=q) |
                            Q(first_name__icontains=q) |
                            Q(speciality__name__icontains=q)
                        )
                    else:
                        continue

                account = Account.objects.filter(generic_query)
            institutes = Institute.objects.filter(year=year)
            faculties = Faculty.objects.filter(institute=None, year=year)
            t = loader.get_template("search.html")
            c = RequestContext(request, {
                'year': year,
                'institutes': institutes,
                'faculties': faculties,
                'account': account,
                'query': request.POST['search_query']})
            return HttpResponse(t.render(c))
        else:
            fuck_year = '/' + str(year) + '/'
        return redirect(fuck_year)
    else:
        fuck_year = '/' + str(year) + '/'
        return redirect(fuck_year)

def year(request):
    year = datetime.now().year
    fuck_year = '/' + str(year) + '/'
    return redirect(fuck_year)

def hello(request, year):
    page = Page.objects.get(slug='main')
    institutes = Institute.objects.filter(year=year)
    faculties = Faculty.objects.filter(institute=None, year=year)
    t = loader.get_template("index.html")
    c = RequestContext(request, {'a': page, 'year': year, 'institutes': institutes, 'faculties': faculties})
    return HttpResponse(t.render(c))

def pages(request, slug, year):
    page = Page.objects.get(slug=slug)
    t = loader.get_template("index.html")
    c = RequestContext(request, {'a': page, 'year': year})
    return HttpResponse(t.render(c))


@login_required
def main(request):
    if request.user.is_secretary or request.user.is_superuser:
        return show_table(request)
    else:
        return show_form(request)


@login_required
def show_form(request):
    if request.method == 'POST':
        account, created = Account.objects.get_or_create(user=request.user)
        account_form = AccountForm(request.POST, request.FILES, instance=account)
        if account_form.is_valid():
            account = account_form.save(commit=False)
            account.date_confirm = datetime.now()
            account.year = datetime.now().year
            account.save()
        return redirect('/accounts/personal/')
    else:
        account, created = Account.objects.get_or_create(user=request.user)
        form = AccountForm(instance=account)
        if account.confirm == 1:
            t = loader.get_template("form.html")
            c = RequestContext(request, {
            'sent': 'Ваше резюме принято!'
            })
            return HttpResponse(t.render(c))
        else:
            t = loader.get_template("form.html")
            c = RequestContext(request, {
                'account': form
            })
            return HttpResponse(t.render(c))


@login_required
def show_table(request):
    account = Account.objects.filter(confirm=1)
    t = loader.get_template("accounts_list.html")
    c = RequestContext(request, {'account': account})
    return HttpResponse(t.render(c))

def specialty(request, id, year):
    spec = Speciality.objects.filter(faculty_id=id)
    institutes = Institute.objects.filter(year=year)
    faculties = Faculty.objects.filter(institute=None, year=year)
    t = loader.get_template("specialty.html")
    c = RequestContext(request, { 'speciality': spec, 'year':year, 'institutes': institutes, 'faculties': faculties })
    return HttpResponse(t.render(c))

def edit(request, id):
    if request.method == 'POST':
        account, created = Account.objects.get_or_create(pk=id)
        account_form = AccountForm(request.POST, request.FILES, instance=account)
        if account_form.is_valid():
            account = account_form.save()
        return redirect('/accounts/personal/')
    else:
        account, created = Account.objects.get_or_create(pk=id)
        form = AccountForm(instance=account)

        t = loader.get_template("edit.html")
        c = RequestContext(request, {
            'account': form,
            'url': request.path
        })
        return HttpResponse(t.render(c))


def user_ajax(request):
    if request.method == 'GET':
        ids = request.GET['id']

    account = Account.objects.get(id=ids)
    t = loader.get_template("ajax_user.html")
    c = RequestContext(request, {'a': account,})
    return HttpResponse(t.render(c))