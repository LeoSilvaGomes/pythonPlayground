from django.db import models
import short_url

class Link(models.Model):
    """Links para serem encurtados"""
    url = models.URLField()
    visualization = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.url)