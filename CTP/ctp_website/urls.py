from django.conf.urls import patterns, url
from ctp_website import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^genre/(?P<genre_name>\w+)/$',views.genre, name = 'genre'),
        url(r'^artists/',views.artists,name = 'artists'),
        url(r'^about/',views.about,name='about'),
        url(r'^contact/',views.contact,name='contact'),
        url(r'^support/',views.support,name='support'),
        url(r'^venues/',views.venues,name='venues'),
        url(r'^tickets/',views.tickets,name='tickets'),
        url(r'^dance/',views.dance,name="dance"),
        url(r'^programme/',views.programme,name = 'programme'),
        url(r'^day/(?P<day_url>\w+)/$',views.day,name = 'day'),
        url(r'^gig/(?P<gig_url>\w+)/$',views.gig,name = 'gig'),
        url(r'^venue/(?P<venue_url>\w+)/$',views.venue,name = 'venue'),
        url(r'^counts/',views.counts,name='counts'),
        url(r'^test/',views.test,name='test'),
        )