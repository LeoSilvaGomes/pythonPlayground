from django.db import models

class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.text

class Entry(models.Model):
    """Algo especifico aprendido sobre um assunto"""
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        if(len(self.text) < 50):
            return self.text
        else:
            return self.text[:50] + '...'

class Url(models.Model):
    """Url que irei formatar caralho"""
    url = models.URLField()
    short_url = models.URLField(default='')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if(len(self.url) < 50):
            return self.url
        else:
            return self.url[:50] + '...'
