from django import forms

from .models import Topic, Url

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['url']