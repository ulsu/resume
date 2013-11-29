# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

class Account(models.Model):
    user = models.ForeignKey('accounts.User', verbose_name='Пользователь')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия', blank=True, null=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя', blank=True, null=True)
    middle_name = models.CharField(max_length=255, verbose_name='Отчество', blank=True, null=True)

    def photo_path(self, filename):
        return 'photos/%s.jpg' % self.pk
    photo = models.ImageField( verbose_name='Фото пользователя', upload_to=photo_path, blank=True, null=True)

    phone = models.CharField(max_length=255, verbose_name='Телефон', blank=True, null=True)
    mail = models.CharField(max_length=255, verbose_name='Электронная почта', blank=True, null=True)
    address = models.TextField(verbose_name='Адрес проживания', blank=True, null=True)
    sait = models.CharField(max_length=255, verbose_name='Личный сайт, блок', blank=True, null=True)
    scope = models.TextField(verbose_name='Предпочтительная сфера деятельности', blank=True, null=True)
    date = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    education = models.ForeignKey('Education', verbose_name='Уровень образования', blank=True, null=True)
    faculty = models.ForeignKey('Faculty', verbose_name='Название факультета', blank=True, null=True)
    speciality = models.ForeignKey('Speciality', verbose_name='Название специальности', blank=True, null=True, related_name='accounts')
    date_of_receipt = models.DateField(verbose_name='Дата поступления', blank=True, null=True)
    expiration_date = models.DateField(verbose_name='Дата окончания', blank=True, null=True)
    other_information = models.TextField(verbose_name='Прочие сведения', blank=True, null=True)
    additional_education = models.TextField(verbose_name='Дополнительное образование', blank=True, null=True)
    experience = models.TextField(verbose_name='Опыт работы', blank=True, null=True)
    skills = models.TextField(verbose_name='Навыки', blank=True, null=True)
    honor = models.TextField(verbose_name='Участие в конференциях,конкурсах научных проектов, награды, публикации')
    languages = models.TextField(verbose_name='Знание языков', blank=True, null=True)
    quality = models.TextField(verbose_name='Личные качества', blank=True, null=True)
    approve = models.BooleanField(verbose_name='Подтвердить')
    confirm = models.BooleanField(verbose_name='Подтверждено студентом')


class Institute(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название института')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'институт'
        verbose_name_plural = 'институты'


class Faculty(models.Model):
    institute = models.ForeignKey(Institute, blank=True, null=True, related_name='faculties')
    name = models.CharField(max_length=255, verbose_name='Название факультета')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'факультет'
        verbose_name_plural = 'факультеты'


class Speciality(models.Model):
    faculty = models.ForeignKey(Faculty, related_name='specialities')
    name = models.CharField(max_length=255, verbose_name='Название специальности')

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
    name = models.CharField(max_length=255, verbose_name='Название страницы')
    content = models.TextField(verbose_name='Контент страницы', blank=True, null=True)