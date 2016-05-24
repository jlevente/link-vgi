import psycopg2
from datetime import datetime, timedelta
from instagram.client import InstagramAPI
import params
import csv

DATE_LIMIT = datetime(2016, 5, 1)

class InstaHandler(object):
    def __init__(self):
        # Connect to Instagram API
        self.orig_client = True
        # Set parameters in params.py
        self.api = InstagramAPI(access_token=params.access_token, client_secret=params.client_secret)
        self.itercount = 0
        self.PHOTO_LIST = []
        self.LOCATION_LIST = []

    def find_locations(self, lat, lng, radius):
        try:
            locations = self.api.location_search(lat=lat, lng=lng, distance=radius, count=33)
            #print(len(locations))
            # If response hits the limit
            # Limit = 33
            if len(locations) == 33:
                print 'Response hits limit of 33. Not all locations were returned.'
            for loc in locations:
                self.LOCATION_LIST.append({
                    "name": loc.name,
                    "id": loc.id,
                    "lat": loc.point.latitude,
                    "lon": loc.point.longitude
                })
        except Exception as e:
            print e
            if e.status_code == '429':
                print 'Limit exceeded.'

    def photo_in_location(self, location_id, max_id):
        try:
            if max_id == 0:
                medias = self.api.location_recent_media(location_id=location_id, count=33)
            else:
                medias = self.api.location_recent_media(location_id=location_id, max_id=max_id, count=33)
            self.itercount += 1
        except Exception, e:
            print e
            if e.status_code == '429':
                print 'Limit exceeded.'

        # Check if there are more photos to download
        if len(medias[0]) > 0:
            cont = True
            print medias[0][0].location.name
            for media in medias[0]:
                # Discard videos now
                if media.type == 'image':
                    tags_arr = []
                    for tag in media.tags:
                        tags_arr.append(tag.name)
                    caption = media.caption
                    if caption == None:
                        text = None
                    else:
                        text = caption.text
                    try:
                       self.PHOTO_LIST.append({
                            "id": media.id.split('_')[0],
                            "username": unicode(media.user.username).encode('utf8'),
                            "user_id": media.user.id,
                            "likes": media.like_count,
                            "comments": media.comment_count,
                            "tagged_users": len(media.users_in_photo),
                            "filter": media.filter,
                            "caption": unicode(text).encode('utf8'),
                            "url": media.link,
                            "photo_url": media.images['standard_resolution'].url,
                            "location_id": media.location.id,
                            "created_at": str(media.created_time),
                            "tags": tags_arr
                        })
                    except AttributeError:
                        continue
                    if media.created_time < DATE_LIMIT or self.itercount > 5:
                        cont = False

            # Recursively continue downloading, pass last media id
            if cont:
                self.photo_in_location(location_id, media.id.split('_')[0])

    def dump_csv(self):
        hashtags = []
        with open ('locations.csv', 'wb') as csvfile:
            fieldnames = ["id", "name", "lat", "lon"]
            writer = csv.DictWriter(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, fieldnames=fieldnames)
            writer.writeheader()
            for location in self.LOCATION_LIST:
                try:
                    writer.writerow(location)
                except UnicodeEncodeError, e:
                    continue
        csvfile.close()

        with open('photos.csv', 'wb') as csvfile:
            fieldnames = ["id", "username", "url", "photo_url", "created_at", "caption", "tagged_users", "likes", "comments", "filter","location_id"]
            writer = csv.DictWriter(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, fieldnames=fieldnames)
            writer.writeheader()
            for photo in self.PHOTO_LIST:
                for hashtag in photo['tags']:
                    hashtags.append(hashtag)
                # Skip special Unicode characters for now
                try:
                    writer.writerow({key:value for key, value in photo.items()if key in fieldnames})
                except UnicodeEncodeError, e:
                    continue
        csvfile.close()

        # Simplest way to dump csv without csv module
        file = open('hashtags.csv', 'wb')
        for hashtag in hashtags:
            try:
                file.write(hashtag + '\n')
            except UnicodeEncodeError:
                continue
        file.close()

handler = InstaHandler()

center_points = [(60.1698712,24.9533877), (60.1673931,24.9459235)]

# Set search radius to 100 m
radius = 100

for point in center_points:
    handler.find_locations(lat=point[0], lng=point[1], radius=radius)

for location in handler.LOCATION_LIST:
    handler.itercount = 0
    id = location['id']
    handler.photo_in_location(id, max_id=0)

handler.dump_csv()
