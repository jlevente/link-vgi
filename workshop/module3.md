## Module 3: Extracting summary statistics from an R environment

This module aims to illustrate some aspects of integrating data gathered from APIs in an R environment for further processing.
In general, once we exported our data from the APIs in a more standardized format, we are able to process it with any statistics software. The purpose of this step is to
data exploration, creating charts and applying statistical tests.

We will use data from Instagram API that contains information of photos posted to Instagram since January 1, 2015 in downtown Helsinki. You can use the sample dataset of
[Instagram locations](../examples/locations.csv) and [Instagram photo metadata](../examples/photos.csv). These data filest were generated with this [script](../examples/insta.py)). Try running it at home.

Using this data allows us to extract insights about popular places in Helsinki, we can quantify data upload intensity and ultimately. Let's do this step by step.

## Data import

The importance of this step is to actually load the data into R. Since we already know how the data is structured, we can run the following lines of code.
(You can also connect R to PostgreSQL with the [`RPostgreSQL`](link to RPostgreSQL) pacakge, and import many other formats, such as [Shapefile](link to shapefile R), [JSON](link to json).


```Rscript
# Import all modules needed for this module
library('ggplot2')
library('reshape2')

locations <- read.csv('locations.csv', as.is=T, quote="\"")
photos <- read.csv('photos.csv', as.is=T, quote="\"")

-- to include:
    exploratory analysis
    sample linear regression (maybe users in photos vs likes?
    sample maps

```

