from django.db import models

class List(models.Model):
    pass

class Item(models.Model):                   # classes that inherit from models.Model map to tables in the database (ang get auto-generated id attribute -> primary key column in the database)
    text = models.TextField(default='')     # any other column must be defined explicitly(with default value):  this is a text field
    list = models.ForeignKey(List, default=None)
