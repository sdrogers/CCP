from django.conf.urls import patterns, url
from ctp_website import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^artist/(?P<artist_name_url>\w+)/$', views.artist, name = 'artist'),
        url(r'^genre/(?P<genre_name>\w+)/$',views.genre, name = 'genre'),
        url(r'^artists/',views.artists,name = 'artists'),
        url(r'^about/',views.about,name='about'),
        url(r'^programme/',views.programme,name = 'programme')
        )