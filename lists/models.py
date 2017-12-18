from django.db import models
from django.core.urlresolvers import reverse

class List(models.Model):
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

class Item(models.Model):                   # classes that inherit from models.Model map to tables in the database (ang get auto-generated id attribute -> primary key column in the database)
    text = models.TextField(default='')     # any other column must be defined explicitly(with default value):  this is a text field
    list = models.ForeignKey(List, default=None)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text
