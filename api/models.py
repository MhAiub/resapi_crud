from django.db import models


class View(models.Model):
    id = models.CharField(max_length=100, blank=True,primary_key=True )
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
