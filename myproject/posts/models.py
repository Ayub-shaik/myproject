from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

#adding a method to our post class, 
#a method is like a function except its part of a class
    
    def __str__(self):
        return self.title