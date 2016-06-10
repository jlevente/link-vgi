# Link‐VGI
**LINKing and analyzing Volunteered Geographic Information (VGI) across different platforms**

Public repository of the [Link-VGI](http://www.geog.uni-heidelberg.de/gis/link_vgi.html) pre-conference workshop at [AGILE2016](https://agile-online.org/index.php/conference/conference-2016).

13 June, 2016. Helsinki, Finland

## Hands-on exercises

The purpose of the hands-on session is to cover the basics of interacting with APIs and to extract summary statistics from the datasets acquired.
All materials can be found in the [Tutorial](workshop/tutorial.md).

## Requirements

You will need to install the following software components before attending the hands-on session.

### Python 2.7

Follow the guides of [this page](https://wiki.python.org/moin/BeginnersGuide/Download) to install a Python version suitable for your operating system.

#### Python modules

###### python-instagram

###### Tweepy - Twitter for Python!

Tweepy is a Python wrapper built around Twitter API. It allows us to easily interact with Twitter data in a Python environment.  You can install Tweepy from PyPi using `easy_install` or `pip`

```
pip install tweepy
```

###### pyshp - Pure Python read/write support for ESRI Shapefile format

This python package allows to read and write regular shapefiles in a Python environment. Use the prebuilt package from PyPi with `easy_install` or `pip`.

```
pip install pyshape
```

####### psycopg2 - PostgreSQL client for Python

It is recommended to install `psycopg2` from a prebuilt package for your Operating System. Some help can be found [here](initd.org/psycopg/docs/install.html).

**Linux (Ubuntu/debian)**

In general the package for Linux distributuions is called `python-psycopg2`. On Debian/Ubuntu, simply run

```
sudo apt-get install python-psycopg2
```

**Mac OS X**

```
fink install psycopg2-py27
```
or
```
sudo port install py27-psycopg2
```

**Windows**

Use an installer for `win-psycopg` from [here](www.stickpeople.com/projects/python/win-psycopg).

###### python-flickrapi
Info can be found [here](https://pypi.python.org/pypi/flickrapi). Install using pip

```
pip install flickrapi
```

### R Statistics

You can follow numerous guides out there to download and install R.

#### Ubuntu

```
sudo apt-get update
sudo apt-get install r-base
```

#### Windows

Download the installer from [here](https://cran.r-project.org/bin/windows/base/) and follow the steps.

#### Mac OSX

Download the pacakge from [here](https://cran.rstudio.com/bin/macosx/) and follow the steps.

### Installing an IDE

You can use any available IDEs. However, RStudio is recommended. You can find the installer packages [here](https://www.rstudio.com/products/rstudio/download/)

### R Packages

Install the following R packages.

```rscript
install.packages('ggplot2')
install.packages('lubridate')
install.paclages('plyr')
install.packages('Reshape2')
```

### QGIS [optional]
QGIS can be used for analysing a number of the datasets obtained within this workshop. As well as being suitable for creating visualisations and assessments of the data, a plugin has also been developed that can be used for viewing images identified from the datasources such as Flickr and Mapillary. 
#### Image Viewer Plugin
To install this plugin, go to Plugins->manage and Install Plugins and then under "Settings" - "Plugin repositories" add a new repository with the URL of http://cap4navi.geog.uni-heidelberg.de/link-vgi/qgis-plugins/qgis-repo.xml , along with a name (it doesn't matter what name you use, this is just so you can identify where the plugins come from) followed by clicking the "OK" button. Right click on the newly added entry (there should be a green icon next to it and the text "connected") and choose "Only show plugins from selected repository". This will make it easier to find the plugin. Also, make sure that the "Show experimental plugins" checkbox on the settings page has been checked. Now go to "Uninstalled", click on the Image Viewer plugin and select install.

To use the plugin, either click on the new icon in the toolbar (a yellow square with a small arrow and camera) or select it from the Plugins->Image Viewer menu. You will also need to have imported the csv files with the actual points in as layers. When the plugin window is open, select from the drop down box which type of image you are going to be selecting (Mapillary, Flickr or Instagram) and then make sure that the corresponding layer has been selected in the Layers panel of QGIS. Now, when you click on one of the points form this layer, the image will be shown in the plugin window.

### API Keys

A number of examples require the use of APIs for acquiring data and often these require an API key to be provided. To save time in the practical it would be of benefit to sign up for and acquire an API key for the following services:

| Service | Registration address | API address |
| ------- | -------------------- | ----------- |
| Wheelmap.org | [http://wheelmap.org/users/sign_in](http://wheelmap.org/users/sign_in) (it is actually OSM you need to register for) | [Edit profile page](http://wheelmap.org/profile/edit)|
| Flickr |[Yahoo](https://login.yahoo.com/account/create?.src=flickrsignup&.scrumb=0&new=1&.pd=c%3DJvVF95K62e6PzdPu7MBv2V8-&.intl=de&.done=https%3A%2F%2Flogin.yahoo.com%2Fconfig%2Fvalidate%3F.src%3Dflickrsignin%26.pc%3D8190%26.scrumb%3D0%26.pd%3Dc%253DJvVF95K62e6PzdPu7MBv2V8-%26.intl%3Dde%26.done%3Dhttps%3A%2F%2Fwww.flickr.com%2Fsignin%2Fyahoo%2F&specId=yidReg&altreg=0) (need to register for Yahoo or use a yahoo account) | [Account settings page](https://www.flickr.com/account/sharing/) and then under "Your API keys" |

If you do not want to sign up for these services, then there will be sample datasets made available, but obviously you will not be able to run the scripts to get data for an area of your choice.

## Testing



