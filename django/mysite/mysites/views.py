from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests
from urllib.parse import quote_plus

from .models import Topic, Url
from .forms import TopicForm, UrlForm

def index(request):
    """Pagina inicial de mysites"""
    return render(request, 'mysites/index.html')

def topics(request):
    """Mostra todos os assuntos."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics' : topics}
    return render(request, 'mysites/topics.html', context)

def topic(request, topic_id):
    """Each topic to visualization"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'mysites/topic.html', context)

def new_topic(request):
    """Adiciona um novo assunto"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mysites:topics'))

    context = {'form' : form}
    return render(request, 'mysites/new_topic.html', context)

def url(request):
    """Pagina com as Urls"""
    urls = Url.objects.order_by('date_added')
    context = {'urls' : urls}
    return render(request, 'mysites/url.html', context)

def new_url(request):
    """Adiciona um url ao assunto"""
    if request.method != 'POST':
        form = UrlForm()
    else:
        form = UrlForm(request.POST)
        if form.is_valid():
            print(60*"*")
            print(form)
            print(60*"*")
            form.save()
            url = form.cleaned_data['url']
            r = requests.get('http://tinyurl.com/api-create.php?url=' + quote_plus(url))
            print(r.text)
            return HttpResponseRedirect(reverse('mysites:url'))
    
    context = {'form': form}
    return render(request, 'mysites/new_url.html', context)