from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    publisher = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        db_table = 'book'
