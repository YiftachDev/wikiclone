#from attr import attrs
from django import forms

class NewArticle(forms.Form):
    title = forms.CharField(label="title", max_length=15, required= True)
    content = forms.CharField(widget=forms.Textarea, required=True, label="content", max_length=200)

class EditArticle(forms.Form):
    content = forms.CharField(widget=forms.Textarea, required=True, label="content", max_length=200)