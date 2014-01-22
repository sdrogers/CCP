from django.contrib import admin
from ctp_website.models import Artist, Gig, Venue, GigDay


class GigAdmin(admin.ModelAdmin):
	list_display = ('artist','date','time')

class DayAdmin(admin.ModelAdmin):
	list_display = ('dayOfTheWeek','date')

admin.site.register(Artist)
admin.site.register(Gig,GigAdmin)
admin.site.register(Venue)
admin.site.register(GigDay,DayAdmin)