from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='main_app/static/uploads/', default= 'pokemon', max_length=100)