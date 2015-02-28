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

class ArtistModelForm(forms.ModelForm):
	bio = forms.CharField(widget=forms.Textarea,required=False)
	class Meta:
		model = Artist

class Venue_Admin(admin.ModelAdmin):
	form = VenueModelForm

class Cab_Admin(admin.ModelAdmin):
	form = CabModelForm
	list_display = ('title','date','time','url','spare')
	
	class Meta:
		model = Gig

class Artist_Admin(admin.ModelAdmin):
	list_display = ('name','instrument')
	form = ArtistModelForm
	filter_horizontal = ('gigs',)
	class Meta:
		model = Artist

class ComposerModelForm(forms.ModelForm):
	bio = forms.CharField(widget=forms.Textarea,required=False)
	class Meta:
		model = Composer

class Composer_Admin(admin.ModelAdmin):
	list_display = ('name','bio')
	form = ComposerModelForm
	class Meta:
		model = Composer

class WorkModelForm(forms.ModelForm):
	bio = forms.CharField(widget=forms.Textarea,required=False)
	class Meta:
		model = Work

class Work_Admin(admin.ModelAdmin):
	list_display = ('name','composer')
	filter_horizontal = ('gigs',)
	form = WorkModelForm
	class Meta:
		model = Work

class SeriesModelForm(forms.ModelForm):
	bio = forms.CharField(widget=forms.Textarea,required=False)
	class Meta:
		model = Series

class Series_Admin(admin.ModelAdmin):
	display = ('name')
	form = SeriesModelForm
	class Meta:
		model = Series

admin.site.register(Gig,Cab_Admin)
admin.site.register(Venue,Venue_Admin)
admin.site.register(GigDay,DayAdmin)
admin.site.register(Artist,Artist_Admin)
admin.site.register(Composer,Composer_Admin)
admin.site.register(Work,Work_Admin)
admin.site.register(Series,Series_Admin)