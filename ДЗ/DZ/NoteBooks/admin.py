from django.contrib import admin
from .models import NoteBook, Manufacturer

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(NoteBook)