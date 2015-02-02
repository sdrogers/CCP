from django.contrib import admin
from ctp_website.models import Gig, Venue, GigDay, Artist, Composer, Work,Series
from django import forms

class GigAdmin(admin.ModelAdmin):
	list_display = ('date','time')

class DayAdmin(admin.ModelAdmin):
	list_display = ('dayOfTheWeek','date')


class CabModelForm( forms.ModelForm ):
    # artist_bio = forms.CharField( widget=forms.Textarea )
    # programme = forms.CharField(widget = forms.Textarea)
    about_programme = forms.CharField(widget = forms.Textarea,required=False)
    # musicians = forms.CharField(widget = forms.Textarea)
    spare = forms.CharField(widget=forms.Textarea,required=False)
    class Meta:
        model = Gig

class VenueModelForm(forms.ModelForm):
	address = forms.CharField(widget = forms.Textarea)
	info = forms.CharField(widget = forms.Textarea)
	class Meta:
		model = Venue

class Venue_Admin(admin.ModelAdmin):
	form = VenueModelForm

class Cab_Admin(admin.ModelAdmin):
	form = CabModelForm
	list_display = ('title','date','time','url','spare')
	
	class Meta:
		model = Gig

class Artist_Admin(admin.ModelAdmin):
	list_display = ('name','instrument')
	class Meta:
		model = Artist

class Composer_Admin(admin.ModelAdmin):
	list_display = ('name','bio')
	class Meta:
		model = Composer

class Work_Admin(admin.ModelAdmin):
	list_display = ('name','composer')
	class Meta:
		model = Work

class Series_Admin(admin.ModelAdmin):
	display = ('name')
	class Meta:
		model = Series

admin.site.register(Gig,Cab_Admin)
admin.site.register(Venue,Venue_Admin)
admin.site.register(GigDay,DayAdmin)
admin.site.register(Artist,Artist_Admin)
admin.site.register(Composer,Composer_Admin)
admin.site.register(Work,Work_Admin)
admin.site.register(Series,Series_Admin)