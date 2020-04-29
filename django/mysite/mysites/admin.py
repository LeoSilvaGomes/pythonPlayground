from django.contrib import admin

from mysites.models import Topic, Entry, Url

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Url)