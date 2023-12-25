from django.db import models

# Create your models here.


class Verbit(models.Model):
    verben = models.CharField('verb-en', max_length=100)
    verbru = models.CharField('verb-ru', max_length=100)
    text = models.TextField('sample', max_length=300)

    def __str__(self):
        return self.verben
