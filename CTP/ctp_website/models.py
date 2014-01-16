from django.db import models

class Genre(models.Model):
	name = models.CharField(max_length = 124, unique = True)
	def __unicode__(self):
		return self.name

class Artist(models.Model):
	name = models.CharField(max_length = 1024, unique = True)
	bio = models.CharField(max_length = 10240)
	genre = models.ForeignKey(Genre)
	url = models.CharField(max_length = 1024)
	# image = models.ImageField(upload_to = 'media',height_field = 'height',width_field = 'width')
	image_url = models.CharField(max_length = 1024,default = "empty")
	image_url2 = models.CharField(max_length = 1024,default = "empty")
	image_width = models.IntegerField(default = "400")
	image_width2 = models.IntegerField(default = "200")
	image_credit = models.CharField(max_length = 1024,default = "empty")
	image_credit2 = models.CharField(max_length = 1024,default = "empty")
	review_url = models.CharField(max_length = 1024,default = "empty")
	review_url2 = models.CharField(max_length = 1024,default = "empty")
	width = models.PositiveIntegerField(blank = True, null = True,editable = False,default = 0)
	height = models.PositiveIntegerField(blank = True, null = True,editable = False,default = 0)
	def __unicode__(self):
		return self.name

class Gig(models.Model):
	artist = models.ForeignKey(Artist)
	date = models.DateField()
	time = models.TimeField()

