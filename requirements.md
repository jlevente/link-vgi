The hands-on session is manily built around the capabilities of the Python programming language and the R statistics software.

# Python 2.7

As a general programming language, Python will serve as our gateway to API interactions. Follow the guides of [this page](https://wiki.python.org/moin/BeginnersGuide/Download) to install a Python version suitable for your operating system.

### Installing a Python IDE

Some graphical interfaces for Python would be useful, however they are not necessary. Just to name a few, IDLE (that comes with most Python installation on Windows and Mac), [PyScripter](https://sourceforge.net/projects/pyscripter/) or
[Eric](http://eric-ide.python-projects.org/eric-download.html). You can of course use any other IDEs depending on your preferences.

# QGIS [optional]
QGIS can be used for analysing a number of the datasets obtained within this workshop. As well as being suitable for creating visualisations and assessments of the data, a plugin has also been developed that can be used for viewing images identified from the datasources such as Flickr and Mapillary. 

### Image Viewer Plugin
To install this plugin, go to Plugins->manage and Install Plugins and then under "Settings" - "Plugin repositories" add a new repository with the URL of http://cap4navi.geog.uni-heidelberg.de/link-vgi/qgis-plugins/qgis-repo.xml , along with a name (it doesn't matter what name you use, this is just so you can identify where the plugins come from) followed by clicking the "OK" button. Right click on the newly added entry (there should be a green icon next to it and the text "connected") and choose "Only show plugins from selected repository". This will make it easier to find the plugin. Also, make sure that the "Show experimental plugins" checkbox on the settings page has been checked. Now go to "Uninstalled", click on the Image Viewer plugin and select install.

To use the plugin, either click on the new icon in the toolbar (a yellow square with a small arrow and camera) or select it from the Plugins->Image Viewer menu. You will also need to have imported the csv files with the actual points in as layers. When the plugin window is open, select from the drop down box which type of image you are going to be selecting (Mapillary, Flickr or Instagram) and then make sure that the corresponding layer has been selected in the Layers panel of QGIS. Now, when you click on one of the points form this layer, the image will be shown in the plugin window.

# R Statistics

R provides a powerful statistics environment for various tasks. You can follow numerous guides out there to download and install R.

#### Ubuntu

```
sudo apt-get update
sudo apt-get install r-base
```

#### Windows

Download the installer from [here](https://cran.r-project.org/bin/windows/base/) and follow the steps.

#### Mac OSX

Download the pacakge from [here](https://cran.rstudio.com/bin/macosx/) and follow the steps.

### Installing an IDE for R

You can use any available IDEs. However, RStudio is recommended. You can find the installer packages [here](https://www.rstudio.com/products/rstudio/download/).

# PostgreSQL with PostGIS [optional]

Install a stable version (e.g. 9.4) of PostgreSQL and PostGIS depending on your operating system.

### Windows

Windows users should use the application stackbuilder from [EnterpriseDB](http://www.enterprisedb.com/products-services-training/pgdownload) and follow the instructions there. Pay attention to install `PostGIS` spatial extension and `pgAdmin` graphical interface during the installation process as well.

### Linux (Ubuntu/Debian)

You can follow many resources out there. It is recommended to install it as a package. Try for example

```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install postgresql-9.4-postgis-2.1 pgadmin3 postgresql-contrib-9.4 python-psycopg2
```

### Mac OS X

Mac users should use the application stackbuilder from [EnterpriseDB](http://www.enterprisedb.com/products-services-training/pgdownload) and follow the instructions there. Pay attention to install `PostGIS` spatial extension and `pgAdmin` graphical interface during the installation process as well.

# Python modules

On top of Python, we are going to use some additional packages as well that makes programming easier. These additional packages are usually developed for a specific purpose (e.g. to interact with Twitter or to handle HTTP requests in general).

#### Tweepy - Twitter for Python!

Tweepy is a Python wrapper built around Twitter API. It allows us to easily interact with Twitter data in a Python environment.  You can install Tweepy from PyPi using `easy_install` or `pip`

```
pip install tweepy
```

#### pyshp - Pure Python read/write support for ESRI Shapefile format

This python package allows to read and write regular shapefiles in a Python environment. Use the prebuilt package from PyPi with `easy_install` or `pip`.

```
pip install pyshape
```

#### psycopg2 - PostgreSQL client for Python

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

#### python-flickrapi
Info can be found [here](https://pypi.python.org/pypi/flickrapi). Install using pip

```
pip install flickrapi
```

##### python-instagram [optional]

*As of June 1, 2016 access to the Instagram API has been seriously cut down by Instagram. You can still install this API wrapper and experiment with it but data access is extremely limited.*
```
pip install python-instagram
```

# R Packages

We are going to use the following R packages. Open an R session and type run following lines.

```Rscript
install.packages('ggplot2')
install.packages('lubridate')
install.paclages('plyr')
install.packages('reshape2')
install.packages('ggmap')
install.packages('wordcloud')
```