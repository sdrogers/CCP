from django.db import models

# class Genre(models.Model):
# 	name = models.CharField(max_length = 124, unique = True)
# 	def __unicode__(self):
# 		return self.name

class Artist(models.Model):
	name = models.CharField(max_length = 1024, unique = True)
	bio = models.CharField(max_length = 10240)
	url = models.CharField(max_length = 1024)
	# image = models.ImageField(upload_to = 'media',height_field = 'height',width_field = 'width')
	image_url = models.CharField(max_length = 1024,default = "empty")
	image_url2 = models.CharField(max_length = 1024,default = "empty")
	image_width = models.IntegerField(default = "400")
	image_width2 = models.IntegerField(default = "200")
	image_credit = models.CharField(max_length = 1024,default = "empty")
	image_credit2 = models.CharField(max_length = 1024,default = "empty")
	musicians = models.CharField(max_length = 1024,default = "empty")
	personal_url = models.CharField(max_length = 1024,default = "empty")

	def __unicode__(self):
		return self.name

class Venue(models.Model):
	name = models.CharField(max_length = 1024,unique=True)
	address = models.CharField(max_length = 1024,unique =True)
	contact_number = models.CharField(max_length = 20,null = True)
	url = models.CharField(max_length = 1024,null = True)
	def __unicode__(self):
		return self.name

class GigDay(models.Model):
	date = models.DateField()
	dayOfTheWeek = models.CharField(max_length = 32,default = "empty")
	def __unicode__(self):
		return self.dayOfTheWeek

class Gig(models.Model):
	artist = models.ForeignKey(Artist)
	date = models.ForeignKey(GigDay)
	time = models.TimeField()
	venue = models.ForeignKey(Venue,null=True)
	programme = models.CharField(max_length = 10240,default = "empty")
	about_programme = models.CharField(max_length = 10240,default = "empty")
	review_url = models.CharField(max_length = 1024,default = "empty")
	review_url2 = models.CharField(max_length = 1024,default = "empty")
	review_url3 = models.CharField(max_length = 1024,default = "empty")
	blog_url = models.CharField(max_length = 1024,default = "empty")
	price = models.CharField(max_length = 1024,default = "empty")
	box_office_url = models.CharField(max_length = 1024,default = "empty")
	box_office_url2 = models.CharField(max_length = 1024,default = "empty")
	special_offers = models.CharField(max_length = 1024,default = "empty")
	special_offers2 = models.CharField(max_length = 1024,default = "empty")
	emergency_field = models.CharField(max_length = 10240,default = "empty")

	def __unicode__(self):
		return self.artist



