# Hands-on session of the Link-VGI workshop

## Module 1: Interacting with APIs

An API (Application Programming Interface) standardizes the ways of interaction between software components.
In web environments, it's a well defined request-response system, where client applications make requests towards a server, to which servers respond.
A common practive is having different endpoints for different set of functionalities. For example `http://api.twitter.com/1.1/users` is responsible for operations related to users (e.g. recommending frieds to https://apps.twitter.com/follow), whereas `http://api.twitter.com/1.1/geo` has methods related to the geospatial domain (e.g. searching for Tweets in a given radius).
APIs usually have different, well documented methods (functions) implemented for different funcionalities (e.g. querying data, inserting new data).
These documentations define accepted parameters for each method along with the expected output (response). A response is usually a JSON or XML document that can be further processed.

### Registering API applications

#### Twitter

Navigate to [apps.twitter.com](https://apps.twitter.com/) and click on `Create New App` (requires to be signed in with your Twitter account). Once the account is created you can modify its permissions (e.g. there's no need to have write permissions for an app that only collects data).
You can also generate your app-only tokens for operations that don't require user level authentication.

#### Instagram

Navigate to [instagram.com/developer/](https://www.instagram.com/developer/) and click on `Register Your Application` and `Register a New Client`. Apps starts in Sandbox mode that's ideal for developement, but has lower rate limits.
You can file a submissions to bring your app `Live`, however it is unknown what Instagram's policy is for accepting academic apps. Sandbox mode works with real Instagram data therefore it is suitable for demonstration.

#### Mapillary

Log in at [mapillary.com](http://mapillary.com) and navigate to `Settings` -> `Integrations` -> `Register an application`. Give your app your name, set up additional permissions levels if needed and hit Create. You'll instantly have access to your Client ID and secret that can be included in API requests.

### Authentication

In order to use APIs, these systems often require authentication from the developer's side. This is to protect user's privacy, monitor usage intensity and in general to govern the different levels of data access.
A general guideline is that an application should only be able to execute operations it is authorized for. An example is OpenStreetMap's JOSM editor, where users can access data (e.g. download via API) but are only able to upload changes once logged in with their credentials (i.e. acquired permissions to perform uploads).
Different APIs implemented different authentication systems, some being completely open and public ([Overpass API](http://wiki.openstreetmap.org/wiki/Overpass_API)) and some requiring a registered application before any interaction ([Instagram API](https://www.instagram.com/developer/)).

#### Twitter
##### Application-only authentication
To get basic data access on behalf of an application (see user timelines, search in tweets, get user information). This authentication level does not allow to use `geo` endpoints but is still useful for example mining a single user's timeline.
##### OAuth signed
To interact with Twitter on behalf of a user. The application first needs to obtain an `access token` and `token secret` from Twitter to be able to make authenticated requests.
The idea is to provide Twitter the details of the application and a user, who can decide whether he/she authorizes our application to perform certain operations. Once it's confirmed, neccesary signatures are generated and can be included in the requests.

*** Tweepy example (for personal use) ***

```python
import tweepy

consumer_token = "Your apps token"
consumer_secret = Your apps secret"

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

#### Instagram

#### OpenStreetMap


### API methods

## Module 2: Exporting spatial data from APIs

### GeoJSON

### Shapefile

### PostGIS

## Extracting summary statistics

## Case studies

### Comparing mapping activities of selected users in Mapillary and OpenStreetMap

### Extracting POIs from different sources
