from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Book(models.Model):
    title = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Edition(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=256)
    year = models.IntegerField()
    pages = models.IntegerField()

class Testimonial(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    testimonial = models.TextField()