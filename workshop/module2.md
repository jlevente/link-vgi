## Module 2: Exporting data from APIs

The general idea is to reshape the data structure that is specific for each API and for each method to a standard format that can be integrated in other systems. The process involves looping through our result sets
and adding data of interesting to our output. Outputs can be anything that can be created in programming environments. If our data falls in the geospatial domain, geospatial data formats can be used as well.

*Here are some examples:*

### Plain CSV
```python
'''
Export tweets within a given radius of a center point to a CSV format
username,tweet_id,text,created_at,lat,lon
'''
import tweepy
import csv

# Set your credentials as explained in the Authentication section
consumer_key = "Your consumer key"
consumer_secret = "Your consumer secret"
# Access tokens are needed only for operations that require authenticated requests
access_key = "Authorized access token acquired from a user"
access_secret = "Authorized access token secret"

# Set up your client
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# Get some tweets around a center point (see http://docs.tweepy.org/en/v3.5.0/api.html#API.search)
tweets = api.search(geocode='37.781157,-122.398720,1km')

data = {
    "username": "",
    "tweet_id": "",
    "text": "",
    "created_at": "",
    "lat": "",
    "lon": ""
}
with open("tweet_export.csv", "wb") as csvfile:
    fieldnames = ["username", "tweet_id", "text", "created_at", "lat", "lon"]
    writer = csv.DictWriter(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)
    writer.writeheader()
    for tweet in tweets:
        data["username"] = tweet.user.screen_name
        data["tweet_id"] = tweet.id
        data["text"] = tweet.text.encode('utf-8')
        data["created_at"] = str(tweet.created_at)
        data["lat"] = tweet.geo['coordinates'][0]
        data["lon"] = tweet.geo['coordinates'][1]
        writer.writerow(data)

```

### GeoJSON

```python
'''
Export Instagram locations as a GeoJSON
'''
import python-instagram


```

### Shapefile

### PostGIS