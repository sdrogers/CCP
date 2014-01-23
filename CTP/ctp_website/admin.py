from django.contrib import admin
from ctp_website.models import Gig, Venue, GigDay


class GigAdmin(admin.ModelAdmin):
	list_display = ('artist_name','date','time')

class DayAdmin(admin.ModelAdmin):
	list_display = ('dayOfTheWeek','date')

admin.site.register(Gig,GigAdmin)
admin.site.register(Venue)
admin.site.register(GigDay,DayAdmin)