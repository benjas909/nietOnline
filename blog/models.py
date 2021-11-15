from django.db import models

# Create your models here.
class Iconos(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Tutorial(models.Model):
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    def __str__(self):
        return self.link

class Tag(models.Model):
    name = models.CharField(max_length=100)
    tutorials = models.ManyToManyField(Tutorial)
    def __str__(self):
        return self.name
