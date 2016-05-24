## Module 3: Extracting summary statistics from an R environment

This module aims to illustrate some aspects of integrating data gathered from APIs in an R environment for further processing.
In general, once we exported our data from the APIs in a more standardized format, we are able to process it with any statistics software. The purpose of this step is to
data exploration, creating charts and applying statistical tests.

We will use data from Instagram API that contains information of photos posted to Instagram since January 1, 2015 in downtown Helsinki. You can use the sample dataset of
[Instagram locations](../examples/locations.csv) and [Instagram photo metadata](../examples/photos.csv). These data filest were generated with this [script](../examples/insta.py)). Try running it at home.

Using this data allows us to extract insights about popular places in Helsinki, we can quantify data upload intensity and ultimately. Let's do this step by step.

## Data import

The importance of this step is to actually load the data into R. You can connect R to PostgreSQL with the [`RPostgreSQL`](http://www.r-bloggers.com/r-and-postgresql-using-rpostgresql-and-sqldf/) pacakge, and import many other formats, such as [Shapefile](http://www.r-bloggers.com/shapefiles-in-r/)
or even [JSON](http://www.tutorialspoint.com/r/r_json_files.htm). In our case, the quickest way to get started is to read the CSV files.
Since we have the chance to study how the data is structured, we can come up the following lines of code:


```Rscript
locations <- read.csv('locations.csv', as.is=T, quote="\"")
photos <- read.csv('photos.csv', as.is=T, quote="\"")
# No quoting in this file. Always check source first!
hashtags <- read.csv('hashtags.csv', as.is=T, header=F)
```

This will give us 3 R data frames for the different sets of data we have. You can call the `head()` and `summary()` functions to examine if the data is correctly loaded. At this point, we should be able to
use all the powerful functionalities of R. `nrow(locations)` yields that we have 56 locations from Instagram ready. Let's draw a map of the spatial distribution.

The [`ggmap` *](https://journal.r-project.org/archive/2013-1/kahle-wickham.pdf) package extends the functionality of `ggplot2` with handy tools to managa spatial data, such as loading background tiles.

* D. Kahle and H. Wickham. ggmap: Spatial Visualization with ggplot2. The R Journal, 5(1), 144-161.

```Rscript
library('ggplot2')
library('plyr')
library('wordcloud')
library('ggmap')

center <- c(lon=mean(locations$lon), lat=mean(locations$lat))
background <- get_map(location=center, source='osm', zoom=15)

map <- ggmap(background, extent='device') 

# Entering map to the console draws the background

# Populate with points
map <- map + geom_point(data=locations, aes(x=lon, y=lat), color='green', size=2)

# Heatmap style visualization of density with countour lines
map <- map + stat_density2d(data=locations, aes(x=lon,y=lat, fill = ..level.., alpha = ..level..), geom='polygon', size=.3) + 
    scale_fill_gradient(low='yellow', high='red', guide=F) +
    stat_density2d(data=locations, aes(x=lon, y=lat), bins=5, color='red', size=.3) + 
    scale_alpha(range=c(0, .2), guide=F)

# Finally, we can annotate our plot
map <- map + ggtitle('Instagram locations in Helsinki') + geom_text(data=locations, aes(x=lon, y=lat, label=name), size=5, check_overlap=T)
```
![alt text](../examples/images/instagramlocations.png "Map of Instagram locations")

The great thing about importing mined data is being able to use all the statistics tools that come with the software. Running the following lines tell us how many photos we gathered,
how many unique users posted those and we can also quickly extract the most popular places.

```Rscript
# Total number of photos
nrow(photos)

# Total number of users
length(unique(photos$username))

# Summarizing data by location
# Ceck out also count(), join() and merge() functions!
locations['user_count'] <- NA
locations['photo_count'] <- NA
locations['user_count'] <- sapply(locations$location_id, function(x) length(unique(photos[photos$location_id==x,]$username)))
locations['photo_count'] <- sapply(locations$location_id, function(x) nrow(photos[photos$location_id==x,]))

# Draw histograms to see how popularity of places is distributed
hist(locations$user_count)
hist(locations$photo_count

# Extract top 20 places with most users
plot_data <- locations[order(-locations$user_count),][1:20,]
plot_data <- transform(plot_data[,c('location_name','user_count')], location_name = reorder(location_name, order(user_counts, decreasing=T)))
plot_data <- transform(plot_data[,c('location_name','user_count')], location_name = reorder(location_name, order(user_count, decreasing=T)))
ggplot(plot_data, aes(x=location_name, y=user_count)) + geom_bar(stat='identity') + theme_bw() + theme(axis.text.x=element_text(angle=90), axis.title.x=element_blank()) + ylab('User counts
```
![alt text](../examples/images/top_places.png "Top 20 places by user counts in downtown Helsinki")

Running statistical tests is also easy. For example we can check on the relationship between the number of `users tagged in each photo` and the `likes` photos have.

```Rscript
subset <- photos[photos$tagged_users > 0 & photos$likes > 0,]

# Log transform like counts since they're not normally distributed
likes <- log10(subset$likes)
tagged_users <- subset$tagged_users

# Build simple linear regression
reg <- lm(likes ~ tagged_users)
plot(tagged_users, likes)
abline(reg, col='red')

# Check the summary to see if the relationship is statistically significant
summary(reg)
```
![alt text](../examples/images/regression.png "Linear regression model")

Code to generate wordcloud of hashtags:

```Rscript
hashtag_freq <- count(hashtags)
names(hashtag_freq) <- c("hashtag","freq")
wordcloud(words=hashtag_freq$hashtag, freq=sqrt(hashtag_freq$freq), min.freq=1, max.words=200, rot.per=0.25,colors=brewer.pal(8,"Dark2"))
```
![alt text](../examples/images/wordcloud_helsinki.png "Wordcloud of hashtags")
