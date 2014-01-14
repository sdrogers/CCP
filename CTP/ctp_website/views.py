from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from ctp_website.models import Artist, Genre


def index(request):
	context = RequestContext(request)
	context_dict = {'hello':"hello"}
	return render_to_response('ctp_website/index.html',context_dict,context)

def artist(request,artist_name_url):
	context = RequestContext(request)
	context_dict = {'artist_name_url':artist_name_url}
	a = Artist.objects.get(url__iexact = artist_name_url)
	try:
		a = Artist.objects.get(url__iexact = artist_name_url)
		context_dict['name'] = a.name
		context_dict['genre'] = a.genre
		context_dict['bio'] = a.bio
		context_dict['image_url'] = a.image
		print a.image
	except:
		pass

	return render_to_response('ctp_website/artist.html',context_dict,context)

def artists(request):
	context = RequestContext(request)
	a = Artist.objects.order_by('name')
	context_dict = {'artists':a}
	return render_to_response('ctp_website/artists.html',context_dict,context)

def genre(request,genre_name):
	context = RequestContext(request)
	context_dict = {'name':genre_name}
	try:
		g = Genre.objects.get(name__iexact = genre_name)
		context_dict['foundname'] = genre_name
		a = Artist.objects.filter(genre = g)
		context_dict['artists'] = a
	except:
		pass

	return render_to_response('ctp_website/genre.html',context_dict,context)
