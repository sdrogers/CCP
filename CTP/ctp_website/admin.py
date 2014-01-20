from django.contrib import admin
from ctp_website.models import Genre, Artist, Gig, Venue


class GigAdmin(admin.ModelAdmin):
	list_display = ('artist','date','time')

admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Gig,GigAdmin)
admin.site.register(Venue)