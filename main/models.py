# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from datetime import datetime

class Account(models.Model):
    user = models.ForeignKey('accounts.User', verbose_name='Пользователь', blank=True, null=True)
    last_name = models.CharField(max_length=255, verbose_name='Фамилия', blank=True, null=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя', blank=True, null=True)
    middle_name = models.CharField(max_length=255, verbose_name='Отчество', blank=True, null=True)

    def photo_path(self, filename):
        year = datetime.now().year
        return 'photos/%s/%s.jpg' % (year, self.pk)
    photo = models.ImageField( verbose_name='Фото пользователя', upload_to=photo_path, blank=True, null=True)

    phone = models.CharField(max_length=255, verbose_name='Телефон', blank=True, null=True)
    mail = models.CharField(max_length=255, verbose_name='Электронная почта', blank=True, null=True)
    address = models.TextField(verbose_name='Адрес проживания', blank=True, null=True)
    sait = models.CharField(max_length=255, verbose_name='Личный сайт, блог', blank=True, null=True)
    scope = models.TextField(verbose_name='Предпочтительная сфера деятельности', blank=True, null=True)
    date = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    education = models.ForeignKey('Education', verbose_name='Уровень образования', blank=True, null=True)
    faculty = models.ForeignKey('Faculty', verbose_name='Название факультета', blank=True, null=True)
    speciality = models.ForeignKey('Speciality', verbose_name='Название специальности', related_name='accounts', blank=True, null=True)
    date_of_receipt = models.DateField(verbose_name='Дата поступления', blank=True, null=True)
    expiration_date = models.DateField(verbose_name='Дата окончания', blank=True, null=True)
    other_information = models.TextField(verbose_name='Прочие сведения', blank=True, null=True)
    additional_education = models.TextField(verbose_name='Дополнительное образование', blank=True, null=True)
    experience = models.TextField(verbose_name='Опыт работы', blank=True, null=True)
    skills = models.TextField(verbose_name='Навыки', blank=True, null=True)
    honor = models.TextField(verbose_name='Участие в конференциях,конкурсах научных проектов, награды, публикации', blank=True, null=True)
    languages = models.TextField(verbose_name='Знание языков', blank=True, null=True)
    quality = models.TextField(verbose_name='Личные качества', blank=True, null=True)
    personal_data = models.TextField(verbose_name='Личные данные', blank=True, null=True)
    date_confirm = models.DateField(verbose_name='Дата подтверждения', blank=True, null=True)
    confirm = models.BooleanField(verbose_name='Подтверждено студентом')
    approve = models.BooleanField(verbose_name='Подтвердить')
    year = models.IntegerField(max_length=4, verbose_name='Год выпуска', blank=True, null=True)

class Institute(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название института')
    year = models.IntegerField(max_length=4, verbose_name='Год')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'институт'
        verbose_name_plural = 'институты'


class Faculty(models.Model):
    institute = models.ForeignKey(Institute, blank=True, null=True, related_name='faculties')
    name = models.CharField(max_length=255, verbose_name='Название факультета')
    year = models.IntegerField(max_length=4, verbose_name='Год')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'факультет'
        verbose_name_plural = 'факультеты'


class Speciality(models.Model):
    faculty = models.ForeignKey(Faculty, related_name='specialities')
    name = models.CharField(max_length=255, verbose_name='Название специальности')
    year = models.IntegerField(max_length=4, verbose_name='Год')


    def __unicode__(self):
        return self.name

class Education(models.Model):
    name = models.CharField(max_length=255, verbose_name='Уровень образования')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Уровень образования'
        verbose_name_plural = 'Уровни образования'

class Page(models.Model):
    slug = models.SlugField(max_length=255, verbose_name='Название страницы')
    content = models.TextField(verbose_name='Контент страницы', blank=True, null=True)