import os

def populate():
	with open('example_data.txt') as f:
		content = f.readlines()
	for c in content:
		comps = c.split('\t')
		g = add_genre(comps[1])
		name = comps[0]
		bio = comps[2].rstrip()
		url = name.replace(' ','_')
		addartist(name,bio,g,url)

def add_genre(name):
	g = Genre.objects.get_or_create(name = name)[0]
	return g
def addartist(name,bio,genre,url):
	a = Artist.objects.get_or_create(name = name,bio = bio, genre = genre,url = url)
	return a


if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CTP.settings')
    from ctp_website.models import Artist, Genre
    populate()