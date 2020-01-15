from django.contrib import admin

# Register your models here.

from .models import Tutor, Tutee

admin.site.register(Tutor)
admin.site.register(Tutee)