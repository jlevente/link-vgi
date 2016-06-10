## Module 2: Exporting data from APIs

The general idea is to reshape the data structure that is specific for each API and for each method to a standard format that can be integrated in other systems. The process involves looping through our result sets
and adding data of interesting to our output. Outputs can be anything that can be created in programming environments. If our data falls in the geospatial domain, geospatial data formats can be used as well.

*Here are some examples:*

### Plain CSV

Python code snippet to get tweets within a radius of a given point and write results to a csv file. We can pick any properties from the `Example Result` section of the [API documentation](https://dev.twitter.com/rest/reference/get/search/tweets).
For simplicity, let's export some basic information, like username, tweet id, message of the post, timestamp of post, and a latitude-longitude coordinate pair corresponding to the location.
```python
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
tweets = api.search(geocode='60.1694461,24.9527073,1km')

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
        data["lon"] = tweet.geo['coordinates'][0]
        data["lat"] = tweet.geo['coordinates'][1]
        writer.writerow(data)

```

### GeoJSON

GeoJSON is a common interchange format gaining popularity over the recent years. It is commonly used in web environments to transport geospatial data but most Dekstop GIS software can read and write the format as well. Below is a Python code snippet you can use to extend the [Wheelmap example from Module 1](https://github.com/jlevente/link-vgi/blob/master/workshop/module1.md#methods-using-a-http-object). These few lines of code will let you export the data in a GeoJSON format.

```python
# This method takes a list of WhelmapItems and writes them to a GeoJSON file

def exportWheelmapNodes(node_list, file_name):
    # Init geojson object
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    # Loop through the list and append each feature to the GeoJSON
    for node in node_list:
        # Populate feature skeleton
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [node.lon, node.lat]
            },
            "properties": {
                "name": node.getName(),
                "osm_id": node.osm_id,
                "category": node.category,
                "node_type": node.node_type,
                "accessible": node.accessible
            }
        }

        # Append WheelnodeItem to GeoJSON features list
        geojson["features"].append(feature)

    # Finally write the output geojson file
    f = open(file_name, "w")
    f.write(json.dumps(geojson))
    f.close()

exportWheelmapNodes(items, "wheelmap_nodes.geojson")
```

### Shapefile

Shapefiles are well known to all GIS professionals therefore it is useful to learn how to create them in Python. The Python code snippet below queries for Mapillary photos in a given area and export them as a shapefile. The example uses the [**/search/im**](https://a.mapillary.com/#get-searchim) method from the Mapillary API to access images nearby. Similar to the `urrlib2` package seen in the Wheelmap example, another package called `requests` (*HTTP for Humans*) can be used to handle HTTP requests in the abscence of available API wrapper. This example also uses the `pyshp` package for writing a shapefile.

```python
import requests
import json
import shapefile
from datetime import datetime

mapillary_api_url = "https://a.mapillary.com/v2/"
api_endpoint = "search/im"
client_id = "Your Mapillary Client ID"

request_params = {
    "client_id": client_id,
    "min_lat": 60.1693326154,
    "max_lat": 60.17107241,
    "min_lon": 24.9497365952,
    "max_lon": 24.9553370476,
    "limit": 100
}

# Make a GET requests 
photos = requests.get(mapillary_api_url + api_endpoint + '?client_id=' +  client_id + '&min_lat=60.1693326154&max_lat=60.17107241&min_lon=24.9497365952&max_lon=24.9553370476')
photos = json.loads(photos.text)

# Init shapefile
writer = shapefile.Writer(shapefile.POINT)
writer.autoBalance = 1
writer.field('image_url', 'C')
writer.field('captured_at', 'C')
writer.field('username', 'C')
writer.field('camera_angle', 'C')

# Add each photo to shapefile
for photo in photos:
    writer.point(photo['lon'], photo['lat'])
    writer.record(image_url='http://mapillary.com/map/im/' + photo['key'], username=photo['user'], camera_angle=str(photo['ca']), captured_at=str(datetime.fromtimestamp(photo['captured_at']/1000)))
writer.save('my_mapillary_photos.shp')
file = open(filename + '.prj', 'w')
# Manually add projection file
file.write('GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]')
file.close()
```

### PostGIS [optional]

PostgreSQL is the leading open source Relational Database Management System. The PostGIS extension allows to execute any geospatial operations in a highly customizable manner.
Here's a more complex python script to

1. export locations of obtaining [drinking water](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Ddrinking_water) from OSM's OverpassAPI and
2. place data in a sptially enabled PostgreSQL database.

First, you need to manually create a database and perform some neccesary steps. You can use various methods to achieve this. For example, you can open  the `pgAdmin`, set up a server connection, then Right click `New object` -> `New Database`. Alternatively you can use the `createdb` command line tool or the `CREATE DATABASE dbname` SQL statement.

Once your database is created, you can run the following statements to enable PostGIS extension and create a table for your soon to be mined OSM data.

```sql
-- Add PostGIS extension
CREATE EXTENSION postgis;
-- Add hstore extension to store tags as key-value pairs
CREATE EXTENSION hstore;
-- Init table
CREATE TABLE drinking_water (
    id bigint,
    user varchar,
    user_id int,
    created_at timestamp,
    version int,
    changeset int,
    tags hstore
    
);
-- Add a POINT geometry column to the table
SELECT AddGeometryColumn('drinking_water', 'geom', 4326, 'POINT', 2);
```

Then run the following Python script.

```python
import psycopg2
import json
import requests

# This function callse OverpassAPI and asks for all nodes that contain "amenity"->"drinking_water" tag
 def query_nodes(bbox):
    # OverpassAPI url
    overpassAPI = 'http://overpass-api.de/api/interpreter'

    postdata = '''
    [out:json][bbox:%s][timeout:120];
    (
        node["amenity"="drinking_water"]
    );
    out geom;
    out meta;
    >;
    '''

    # Sending HTTP request toward OverpassAPI
    data = requests.post(overpassAPI, postdata % (bbox))
    # Parse response
    data = json.loads(data.text)
    return data

# This function uploads the data to the PostgreSQL server
def upload_data(data):
    with_no_geom = 0
    sql = 'INSERT INTO drinking_water (id, user, user_id, created_at, version, changeset, tags, geom) VALUES (%s, %s, %s, %s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326));'

    # Define a connection
    conn = psycopg2.connect(host='localhost', user='postgres', password='postgres', dbname='osm_data')
    psycopg2.extras.register_hstore(conn)
    # Initialize a cursor
    cursor = conn.cursor()
    # Loop through all OSM nodes
    for node in data['elements']:
        # Call the INSERT INTO sql statement with data from the current node
        cursor.execute(sql,(node['id'], node['user'], node['uid'], node['timestamp'], node['version'], node['changeset'], node['lon'], node['lat']))
    # Finally commit all changes in the database
    conn.commit()

# Lago Maggiore
bbox = '45.698507, 8.44299,46.198844,8.915405'

# Start with putting all nodes in the variable called drinking_water
drinking_water = query_nodes(bbox)
# Pass this variable containing all OSM nodes to the upload script that will insert it to the PostgreSQL database
upload_data(drinking_water)
```

Alternatively you can visualize your data in QGIS, or you can simply make a query toward the database to see if it worked

```
-- Select 10 nodes
SELECT id, user, created_at, tags from drinking_water limit 10
```
