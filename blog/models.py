from django.db import models

# Create your models here.
class Iconos(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name

class Tutorial(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    tutorials = models.ManyToManyField(Tutorial)
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name
