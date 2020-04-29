from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Link
from .forms import LinkForm

def new_link(request):
    """Pagina Inicial do meu site"""
    if request.method != 'POST':
        form = LinkForm()
    else:
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('encurtador:new_link'))
    
    context = {'form': form}
    return render(request, 'encurtador/home.html', context)

def rank(request):
    """Retorna a lista de links"""
    links = Link.objects.order_by('-visualization')[:5]
    context = {'links' : links}
    return render(request, 'encurtador/rank.html',  context)

def link(request, link_id):
    """Redirect to each site"""
    link = Link.objects.get(id=link_id)
    link.visualization += 1
    link.save()
    return HttpResponseRedirect(link.url)
