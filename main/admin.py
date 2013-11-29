# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *


class AccountAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name')

admin.site.register(Account, AccountAdmin)


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Faculty, FacultyAdmin)


class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Speciality, SpecialityAdmin)

class InstituteAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Institute, InstituteAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Education, EducationAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

admin.site.register(Page, PageAdmin)