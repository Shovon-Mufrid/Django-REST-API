from django.contrib import admin
from .models import Contact
from ckeditor.fields import RichTextField
# Register your models here.

admin.site.register(Contact)