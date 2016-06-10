import flickrapi
import json
import csv
from datetime import date, timedelta

api_key = 'API-KEY'
api_secret = 'SECRET-KEY'

csv_path = 'flickr_helsinki.csv'

class Image:
	def __init__(self, photo_id, lat, lon):
		self.photo_id = photo_id
		self.lat = lat
		self.lon = lon
		self.url = ''

	def setImageUrl(self, url):
		self.url = url

flickr = flickrapi.FlickrAPI(api_key, api_secret)

bbox = '24.899319,60.150223,24.986683,60.177915'

photos = []

count = 0

d = date.today() - timedelta(days=90)

#first get a count
print('Working...')
for photo in flickr.walk(tag_mode='all',bbox=bbox, min_taken_date=d, extras='geo'):
	count = count+1
	if count%10 == 0:
		print '.',

print('\n' + str(count) + ' images found, processing...')

count = 1

for photo in flickr.walk(tag_mode='all', bbox=bbox, min_taken_date=d, extras='geo'):
	print(str(count)),
	count = count+1
	img = Image(photo.get('id'), photo.get('latitude'), photo.get('longitude'))
	# construct url
	img.setImageUrl('https://farm' + photo.get('farm') + '.staticflickr.com/' + photo.get('server') + '/' + photo.get('id') + '_' + photo.get('secret') + '_z.jpg')


	photos.append(img)

print('Writing to csv')	

# output to csv
with open(csv_path, 'w') as csvfile:
	fieldnames = ['photo_id', 'lat', 'lon', 'url']
	wr = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
	wr.writeheader()

	for photo in photos:
		wr.writerow({'photo_id': photo.photo_id, 'lat': photo.lat, 'lon': photo.lon, 'url': photo.url})
