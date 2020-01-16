from django.contrib import admin

# Register your models here.

from .models import Tutor, Tutee

#admin.site.register(Tutor)
#admin.site.register(Tutee)

# Define the admin class
class TutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile_no', 'subjects', 'grade', 'timeslot', 'days')
    list_filter = ('subjects', 'grade')
    fieldsets = (
        ('Tutor', {
            'fields': ('name', 'email', 'mobile_no')
        }),
        ('Subjects', {
            'fields': ('subjects', 'grade')
        }),
        ('Availability', {
            'fields': ('timeslot', 'days')
        }),
    )

# Register the admin class with the associated model
admin.site.register(Tutor, TutorAdmin)

# Define the admin class
class TuteeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile_no', 'subjects', 'timeslot', 'days')
    fieldsets = (
        ('Tutor', {
            'fields': ('name', 'email', 'mobile_no')
        }),
        ('Subjects', {
            'fields': ['subjects']
        }),
        ('Availability', {
            'fields': ('timeslot', 'days')
        }),
    )

# Register the admin class with the associated model
admin.site.register(Tutee, TuteeAdmin)
