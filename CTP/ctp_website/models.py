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
	image = models.ImageField(upload_to = 'media',height_field = 'height',width_field = 'width')

	width = models.PositiveIntegerField(blank = True, null = True,editable = False,default = 0)
	height = models.PositiveIntegerField(blank = True, null = True,editable = False,default = 0)
	def __unicode__(self):
		return self.name

