# Module 1: Interacting with APIs

An API (Application Programming Interface) standardizes the ways of interaction between software components.
In web environments, it's a well defined request-response system, where client applications make requests towards a server, to which servers respond.
A common practive is having different endpoints for different set of functionalities. For example `http://api.twitter.com/1.1/users` is responsible for operations related to users (e.g. recommending frieds to follow), whereas `http://api.twitter.com/1.1/geo` has methods related to the geospatial domain (e.g. searching for Tweets in a given radius).
APIs usually have different, well documented methods (functions) implemented for different funcionalities (e.g. querying data, inserting new data).
These documentations define accepted parameters for each method along with the expected output (response). A response is usually a JSON or XML document that can be further processed.

## Registering API applications

#### Twitter

Navigate to [apps.twitter.com](https://apps.twitter.com/) and click on `Create New App` (requires to be signed in with your Twitter account). Once the account is created you can modify its permissions (e.g. there's no need to have write permissions for an app that only collects data).
You can also generate your app-only tokens for operations that don't require user level authentication.

#### Instagram

Navigate to [instagram.com/developer/](https://www.instagram.com/developer/) and click on `Register Your Application` and `Register a New Client`. Apps starts in Sandbox mode that's ideal for developement, but has lower rate limits.
You can file a submissions to bring your app `Live`, however it is unknown what Instagram's policy is for accepting academic apps. Sandbox mode works with real Instagram data therefore it is suitable for demonstration.

#### Mapillary

Log in at [mapillary.com](http://mapillary.com) and navigate to `Settings` -> `Integrations` -> `Register an application`. Give your app your name, set up additional permissions levels if needed and hit Create. You'll instantly have access to your Client ID and secret that can be included in API requests.

#### Flickr
Log in at [flickr.com](http://flickr.com) and go to the `Sharing & Extending` area of your account settings (click on your profile icon in the top right -> `Settings`-> `Sharing & Extending`). Click on the link next to `Your API keys` and click on `Get another key` followed by `Apply for non-commercial key`. Enter the required information and click the `Submit` button to get a key for use.

## Making requests in a python environment

Altough APIs can be used from any environment that can handle HTPP requests, it is beneficial to make use of existing API wrappers. These wrappers are usually developed based on the API documentation, often by 3rd parties and they
purpose is to tackle some technical challenges for developers, making interactions easier. Using API wrappers in python is an easy way to start with.
Some examples are [Tweepy](https://github.com/tweepy/tweepy) for Twitter, [python-instagram](https://github.com/facebookarchive/python-instagram) for Instagram or even a low level package for [Overpass API](https://github.com/mvexel/overpass-api-python-wrapper).

In some cases however, such as with Wheelmap, easy to use API wrappers are not readily available. In those cases, data can still be obtained relatively easily, though some basic knowledge of HTTP communication is required. The bulk of the HTTP communication can be done through inbuilt packages (urllib2 in Python for example) specifically aimed at facilitating communication of data over HTTP connections in a straightforward manner.

## Authentication

In order to use APIs, these systems often require authentication from the developer's side. This is to protect user's privacy, monitor usage intensity and in general to govern the different levels of data access.
A general guideline is that an application should only be able to execute operations it is authorized for. An example is OpenStreetMap's JOSM editor, where users can access data (e.g. download via API) but are only able to upload changes once logged in with their credentials (i.e. acquired permissions to perform uploads).
Different APIs implemented different authentication systems, some being completely open and public ([Overpass API](http://wiki.openstreetmap.org/wiki/Overpass_API)) and some requiring a registered application before any interaction ([Instagram API](https://www.instagram.com/developer/)).

#### Twitter

###### Application-only authentication
To get basic data access on behalf of an application (see user timelines, search in tweets, get user information).
You only need to include your client's `Consumer Token` and `Consumer Secret` in your requests to use this authenticaiton method. This authentication level does not allow to use `geo` endpoints but is still useful for example mining a single user's timeline.

###### OAuth signed
To interact with Twitter on behalf of a user. The application first needs to obtain an `access token` and `token secret` from Twitter to be able to make authenticated requests.
The idea is to provide Twitter the details of the application and a user, who can decide whether he/she authorizes our application to perform certain operations. Once it's confirmed, neccesary signatures are generated and can be included in the requests.

**Tweepy example (for personal use)**

```python
import tweepy

consumer_token = "Your apps token"
consumer_secret = "Your apps secret"

def get_user_tokens(consumer_token, consumer_secret):
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

    print "Navigate to the following webpage and authorize your application"
    print(auth.get_authorization_url())
    pin = raw_input("Enter the PIN acquired on Twitter website").strip()

    token = auth.get_access_token(verifier=pin)

    access_token = token.key
    token_secret = token.secret
    print "With the following tokens, your application should be able to make requests on behalf of the specific user"
    print "Access token: %s" % access_token
    print "Token secret: %s" % token_secret
    return access_token, token_secret

access_token, token_secret = get_user_tokens(consumer_token, consumer_secret)

```

Since Twitter does not terminate access token credentials, you can re-use them until the user revokes your permissions. Your access token and token secret will be further used in this tutorial.

### Instagram

For basic access, use your `Client ID` and `Client Secret` from your application's page.
To be able to make requests on behalf of a user (or make requests that require this level of authentication), you can use the [get_access_token.py](https://github.com/facebookarchive/python-instagram/blob/master/get_access_token.py) script to generate an `access token`.
You can use `http://localhost` as your Redirect URI and then copy the code from your browser's address bar.

### OpenStreetMap

Most of the API functions work without authentication. However, all calls that try to create, modify or delete any OSM data need to be authenticated (i.e. a user to be logged in).
Consult the Wiki for the [basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) or [OAuth](http://wiki.openstreetmap.org/wiki/OAuth).

### Wheelmap

Although Wheelmap data is primarily based on the OSM dataset, an API key is required for requests. This key needs to be passed in the query string of the HTTP request in the form &api_key=xxx. The key can be obtained from the [user profile](https://wheelmap.org/profile/edit) area of the Wheelmap site after logging in with an OSM account.

### Flickr
For making requests to the Flickr API, an api_key is required for most interaction. After signing in to Flickr, the key can be found in the [Account Settings page](https://www.flickr.com/account/sharing/).

## API methods

API methods are the most important elements of our interactions with data. There are different functionalities defined for every API, together with the list of properties we can use and the expected output of the methods.
When working with a platform, the API documentation is the starting point, where we can figure out what options we have and what methods suit to our needs.
The documentation for [Twitter](https://dev.twitter.com/overview/documentation), [Instagram](https://www.instagram.com/developer/endpoints/), [OSM](http://wiki.openstreetmap.org/wiki/API_v0.6), [Mapillary](https://a.mapillary.com/) or [Facebook Graph](https://developers.facebook.com/docs/graph-api/reference/) can be accessed on each site.
Some services have better documentation than others.

To search for Tweets within an area, we can use [`search/tweets`](https://dev.twitter.com/rest/reference/get/search/tweets) from Twitter REST API with the `geocode` parameter, that consists of a latitude, longitude pair and a radius value.
Here's what it looks like with Tweepy:

```python
import tweepy

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

# Print all tweets
for tweet in tweets:
    print "%s said: %s at %s. Location: %s" % (tweet.user.screen_name, tweet.text, tweet.created_at, tweet.geo['coordinates'])
    print "---"
    
```

### Methods using a HTTP object
As mentioned earlier, not all APIs have a wrapper available to make communication easy. One example of these is Wheelmap. In the case that a wrapper class is not available, data can normally be obtained through direct connection with the API via the internet. Within python, there is the urllib2 inbuilt package that can perform such tasks. When communicating directly with the API, you need to know a few basics first. 
API calls are made up of two components: a request, and a response. The request is sent by the client (our python script) to the API and basically asks for some specific action to be performed. This can be an action such as getting a list of features, creating a new feature or any other process of the service that the API exposes. In our case, we will stick with simply asking for some data. The response componenet is what the API sends back to the client.
So lets look at some code that gets Wheelmap features from the API using a HTTP connector.
```python
import json
import urllib2
import urllib
import csv

api_key = 'xxx'
csv_path = 'wheelmap_heidelberg.csv'

class WheelmapItem:
	def __init__(self, name, osm_id, lat, lon, category, node_type, accessible):
		self.name = name
		self.osm_id = osm_id
		self.lat = lat
		self.lon = lon
		self.category = category
		self.node_type = node_type
		self.accessible = accessible

	def getName(self):
		if not self.name:
			return ''
		else:
			return self.name.encode('utf-8')

def getWheelmapNodes(ll_lat, ll_lon, ur_lat, ur_lon, page, accessible):
	bbox = str(ll_lat) + ',' + str(ll_lon) + ',' + str(ur_lat) + ',' + str(ur_lon)
	url = 'http://wheelmap.org/api/nodes?api_key=' + api_key + '&bbox=' + bbox + '&page=' + str(page)
	if accessible != None:
		url = url + '&wheelchair=' + accessible
	headers = {'User-Agent':'Python'}
	
	req = urllib2.Request(url, None, headers)

	print (url)
	resp = urllib2.urlopen(req).read().decode('utf-8')
	return json.loads(resp)

# When we get the first load of data we can read the meta info to see how many pages there are in total

firstPage = getWheelmapNodes(8.638939,49.397075,8.727843,49.429415,1,None)
numPages = firstPage['meta']['num_pages']

# so now we need to loop through each page and store the info
pagedData = []
pagedData.append(firstPage)

for i in range (2,numPages+1):
	pagedData.append(getWheelmapNodes(8.638939,49.397075,8.727843,49.429415,i,None))

# now that we have the data we should go through and create a list of items 
# for now we will store the name, location, category, node type, accessibility and osm id
items = []
for i in range (0,len(pagedData)):
	page = pagedData[i]
	# go through each item
	nodes = page['nodes']
	for node in nodes:
		item = WheelmapItem(node['name'], node['id'], node['lat'], node['lon'], node['category']['identifier'], node['node_type']['identifier'], node['wheelchair'])
		items.append(item)

print('Total items read: ' + str(len(items)))
```
The first thing to note is the `class WheelmapItem:` class decleration at the beggining of the code. This is a simple class that can be used as a template for Wheelmap features in the script, which makes reading information later on easier.

The `getWheelmapNodes(ll_lat, ll_lon, ur_lat, ur_lon, page, accessible):` is the method that we have written to actually get the data from the API. Let's look more in depth at that method now.

```python
def getWheelmapNodes(ll_lat, ll_lon, ur_lat, ur_lon, page, accessible):
	bbox = str(ll_lat) + ',' + str(ll_lon) + ',' + str(ur_lat) + ',' + str(ur_lon)
	url = 'http://wheelmap.org/api/nodes?api_key=' + api_key + '&bbox=' + bbox + '&page=' + str(page)
	if accessible != None:
		url = url + '&wheelchair=' + accessible
	headers = {'User-Agent':'Python'}
	
	req = urllib2.Request(url, None, headers)

	print (url)
	resp = urllib2.urlopen(req).read().decode('utf-8')
	return json.loads(resp)
```
The first step is to create a bounding box string that is passed to the API as a means of identifying what area to get features for `bbox = str(ll_lat) + ',' + str(ll_lon) + ',' + str(ur_lat) + ',' + str(ur_lon)`.
Next we create the URL that is used to request the data. This URL is exactly the same as what you would type into a web browser to get the same information. In this URL (and many many others) we can provide parameters within the URL itself. This part of the URL is known as the "query string". The start of the query string always starts with a ? symbol, and each parameter consists of a name=value pair. If more than one parameter is used, then they are seperated using the & symbol. For example, say we wanted to get a list from a service that tells us who dies in Game of Thrones (it would be a very long list...). The URL may be something like `http://www.whodiesingot.com/deaths?house=stark&book_number=2` (don't worry, I won't give any spoilers). The important part here is the `deaths?house=stark&book_number=2` which is a call to the 'deaths' API method. Notice the ? symbol which tells the `deaths` API method that we are giving it some parameters. the two parameters (seperated by &) are `house=stark` and `book_number=2`. This means that we are telling the service that we want a list of all deaths from the house of Stark which happen in the second book.
In the case of the Wheelmap API we are required to provide three pieces of information: our api key that we obtain from our user profile, the bounding box which tells it where to get features for, and the page number. As most APIs only return a limited number of features per request, they often paginate the data. This means that say, for example, there were 1000 features found in the bounding box, but the service is limited to only provide 100 per request, it would split the dataset into 10 groups of 100, known as pages. In the first response it would send the first 100 (1-100) but would also provide extra information in the response telling the requesting client that this is a subset of all the data (i.e. `items_per_page=100,total_pages=10,current_page=1`). The client then knows that it should make another request to the API, but this time tell it to get the second page (features 101-200), and then a third request to get the third (201-300) and so on. 
The Wheelmap API also allows you to specify what level of accessibility of features we are looking for. Providing the vale `accessible=yes` tells it to return only the accessible places, whereas `accessible=unknown` tells it to only get the unknown ones. The other two values are 'no' and 'limited'. As this is an optional parameter, our code only puts it on to the request if there is an explicit need for it, i.e. we tell the method we want only those places that are accessible. Without the parameter, Wheelmap returns all features in the bounding area.
The `headers = {'User-Agent':'Python'}` line is often required as many services need to have where the request is coming from provided. If you enter the url in a browser, this information is automatically put on to the request, but not when you do it through a script.
Now we construct the request to the service with `req = urllib2.Request(url, None, headers)`. url is the URL that we created above, None tells the method that we are not passing any extra parameters that are not in the query string of the URL, and headers is the user-agent information identifying to the API where the request is coming from. At this point, no data is being transmitted. 
To make the request for information, we use `resp = urllib2.urlopen(req).read().decode('utf-8')`. This line tells the urllib2 package to open a connection to the API as specified in the Request (req) object we just created, then read what is sent back and decode the information to a particular string format. resp now contains a string representation of a JSON object detailing the features returned by the request to the API. The `json.loads(resp)` line just tells the system that we want the response changed to a JSON object in the script.

Now that we know how the requesting works, we have the code that actually calls this method to make the requests. First we obtain the first page of the data (pages are described above) with the line `firstPage = getWheelmapNodes(8.638939,49.397075,8.727843,49.429415,1,None)`.
Once we have data from the request, we need to see if there are any additional pages that need to be read. We get this information using `numPages = firstPage['meta']['num_pages']`. This looks into the JSON data we got from the response, finds a JSON object called 'meta' and then gets the value of the 'num_pages' property. Now that we have the number of pages, the next few lines repeat the request process until all pages have been stored in the pagedData array.

The final stage of reading from the API is to go through all the data we have obtained and convert them into WheelmapItems for easier use later on.
