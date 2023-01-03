from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    title= models.CharField(max_length=200)
    email= models.CharField(max_length=100)
    details=RichTextField(null=True)

    def __str__(self):
        return self.name