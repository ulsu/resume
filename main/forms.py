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
                field.widget = forms.DateInput(attrs={'placeholder': field.label, 'class': 'datepicker', 'required': 'required'})
            if type(field.widget) == forms.Textarea:
                field.widget = forms.Textarea(attrs={'placeholder': field.label})
            if field.widget in ['last_name','first_name','date','education','faculty','speciality']:
                field.widget.attrs['required'] = 'required'

        self.fields['faculty'].queryset = Faculty.objects.filter(year=datetime.now().year)
        self.fields['speciality'].queryset = Speciality.objects.filter(year=datetime.now().year)

