from django import forms
from app.models import *


class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=100)

class WebpageForm(forms.Form):
    topic_name=forms.ChoiceField()
    name=forms.CharField(max_length=100)
    url=forms.URLField()

class AccessRecordForm(forms.Form):
    name=forms.ChoiceField()
    date=forms.DateField()
    author=forms.CharField(max_length=100)

