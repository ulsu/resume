# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
import datetime
from models import *

class AccountForm(ModelForm):
    class Meta:
        model = Account
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            field = self.fields.get(f)
            if type(field.widget) == forms.TextInput:
                field.widget = forms.TextInput(attrs={'placeholder': field.label})
            if type(field.widget) == forms.DateInput:
                field.widget = forms.DateInput(attrs={'placeholder': field.label, 'class': 'datepicker'})
            if type(field.widget) == forms.Textarea:
                field.widget = forms.Textarea(attrs={'placeholder': field.label})
