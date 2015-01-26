#! encoding=utf-8

from django.forms import ModelForm
from django import forms
from fdyouth.models import *

class academy_form(ModelForm):
    class Meta:
        model = academy
        fields = '__all__'

class news_form(ModelForm):
    class Meta:
        model = news
        fields = '__all__'

class life_form(ModelForm):
    class Meta:
        model = overseas 
        fields = '__all__'

class academy_search_form(forms.Form):
    title = forms.CharField(max_length=255)
    begin_date = forms.DateTimeField()
    end_date = forms.DateTimeField()
    author = forms.CharField(max_length=255)
    field = forms.CharField(max_length=255)
    keyword = forms.CharField(max_length=255)
    issue = forms.IntegerField()

class life_search_form(forms.Form):
    title = forms.CharField(max_length=255)
    begin_date = forms.DateTimeField()
    end_date = forms.DateTimeField()
    author = forms.CharField(max_length=255)
    place = forms.CharField(max_length=255)
    keyword = forms.CharField(max_length=255)
    issue = forms.IntegerField()

class news_search_form(forms.Form):
    title = forms.CharField(max_length=255)
    begin_date = forms.DateTimeField()
    end_date = forms.DateTimeField()
    keyword = forms.CharField(max_length=255)
