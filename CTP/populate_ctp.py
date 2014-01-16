import os

def populate():
	with open('example_data.txt') as f:
		content = f.readlines()
	for c in content:
		print c
		comps = c.split('\t')
		g = add_genre(comps[1])
		name = comps[0].rstrip()
		bio = comps[2].rstrip()
		url = name.replace(' ','_')
		if len(comps)>3:
			image_url = comps[3].rstrip()
			image_credit = comps[4].rstrip()
		else:
			image_url = "empty"
			image_credit = "empty"

		if len(comps)>5:
			image_url2 = comps[5].rstrip()
			image_credit2 = comps[6].rstrip()
		else:
			image_url2 = "empty"
			image_credit2 = "empty"

		if len(comps)>7:
			review_url = comps[7].rstrip()
		else:
			review_url = "empty"


		addartist(name,bio,g,url,image_url,image_url2,review_url,image_credit,image_credit2)

def add_genre(name):
	g = Genre.objects.get_or_create(name = name)[0]
	return g
def addartist(name,bio,genre,url,image_url,image_url2,review_url,image_credit,image_credit2):
	a = Artist.objects.get_or_create(name = name,bio = bio, genre = genre,url = url,image_url = image_url,image_url2 = image_url2,review_url = review_url,image_width = 400,image_width2 = 200,image_credit = image_credit,image_credit2 = image_credit2)
	return a


if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CTP.settings')
    from ctp_website.models import Artist, Genre
    populate()