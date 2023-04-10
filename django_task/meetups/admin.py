from django.contrib import admin
from .models import Meetup , Location , Participant

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display=('titele' ,'date' , 'Location')
    list_filter = ('Location' , 'date')
    prepopulated_fields ={'slug':('titele',)}

admin.site.register(Meetup , MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)