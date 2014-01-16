from django.contrib import admin
from ctp_website.models import Genre, Artist, Gig


class GigAdmin(admin.ModelAdmin):
	list_display = ('artist','date','time')

admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Gig,GigAdmin)