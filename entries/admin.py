from django.contrib import admin
from .models import Entry, Person

admin.site.register(Person)
admin.site.register(Entry)
