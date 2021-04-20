# -*- coding: utf-8 -*-
from django import forms
from app.models import *
from django.forms import (
    IntegerField, DateTimeInput, TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, DateTimeField, FloatField
)


class BookForm(forms.ModelForm):
    """
    Form that manages the books model fields
    """
    title = forms.CharField(widget=TextInput(attrs={
        'class':'mat-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = True)

    author = forms.CharField(widget=TextInput(attrs={
        'class':'mat-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = True)

    pages = forms.CharField(widget=TextInput(attrs={
        'class':'mat-input',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = True)

    class Meta:

        model = Book

        fields = [
            'title',
            'author',
            'pages',
        ]
