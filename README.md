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

### Python modules

#### python-instagram

#### python-facebook [optional for mapping_behavior example]

#### [python-flickrapi](https://pypi.python.org/pypi/flickrapi) - https://pypi.python.org/pypi/flickrapi

```
pip install flickrapi
```

### R Statistics

You can follow numerous guides out there to download and install R.

#### Ununtu

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

### API Keys

A number of examples require the use of APIs for acquiring data and often these require an API key to be provided. To save time in the practical it would be of benefit to sign up for and acquire an API key for the following services:

| Service | Registration address | API address |
| ------- | -------------------- | ----------- |
| Wheelmap.org | [http://wheelmap.org/users/sign_in](http://wheelmap.org/users/sign_in) (it is actually OSM you need to register for) | [Edit profile page](http://wheelmap.org/profile/edit)|
| Flickr |[Yahoo](https://login.yahoo.com/account/create?.src=flickrsignup&.scrumb=0&new=1&.pd=c%3DJvVF95K62e6PzdPu7MBv2V8-&.intl=de&.done=https%3A%2F%2Flogin.yahoo.com%2Fconfig%2Fvalidate%3F.src%3Dflickrsignin%26.pc%3D8190%26.scrumb%3D0%26.pd%3Dc%253DJvVF95K62e6PzdPu7MBv2V8-%26.intl%3Dde%26.done%3Dhttps%3A%2F%2Fwww.flickr.com%2Fsignin%2Fyahoo%2F&specId=yidReg&altreg=0) (need to register for Yahoo or use a yahoo account) | [Account settings page](https://www.flickr.com/account/sharing/) and then under "Your API keys" |

If you do not want to sign up for these services, then there will be sample datasets made available, but obviously you will not be able to run the scripts to get data for an area of your choice.

## Testing



