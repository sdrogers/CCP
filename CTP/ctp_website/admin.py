from django.contrib import admin
from ctp_website.models import Gig, Venue, GigDay
from django import forms

class GigAdmin(admin.ModelAdmin):
	list_display = ('artist_name','date','time')

class DayAdmin(admin.ModelAdmin):
	list_display = ('dayOfTheWeek','date')


class CabModelForm( forms.ModelForm ):
    artist_bio = forms.CharField( widget=forms.Textarea )
    programme = forms.CharField(widget = forms.Textarea)
    about_programme = forms.CharField(widget = forms.Textarea)
    musicians = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = Gig

class VenueModelForm(forms.ModelForm):
	address = forms.CharField(widget = forms.Textarea)
	info = forms.CharField(widget = forms.Textarea)
	class Meta:
		model = Venue

class Venue_Admin(admin.ModelAdmin):
	form = VenueModelForm

class Cab_Admin( admin.ModelAdmin ):
    form = CabModelForm

admin.site.register(Gig,Cab_Admin)
admin.site.register(Venue,Venue_Admin)
admin.site.register(GigDay,DayAdmin)