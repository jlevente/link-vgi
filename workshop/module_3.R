# Set your workspace directory
setwd('/home/jlevente/gisdata/link-vgi/examples/data_files')

# Load packages
library('ggplot2')
library('plyr')
library('wordcloud')
library('ggmap')

# Load Instagram data
locations <- read.csv('locations.csv', as.is=T, quote="\"")
photos <- read.csv('photos.csv', as.is=T, quote="\"")
# No quoting in this file. Always check source first!
hashtags <- read.csv('hashtags.csv', as.is=T, header=F)

###################################
# Generating a map of locations   #
###################################

# Set map center to the arithmetic mean of lat-long coordinates
center <- c(lon=mean(locations$lon), lat=mean(locations$lat))
# Init map background to OpenStreetMap tiles at zoom level 15
background <- get_map(location=center, source='osm', zoom=15)

# Create a ggmap object
map <- ggmap(background, extent='device') 

# Hint: typing map to the console (calling your object) will print out the background map

# Populate map plot with points using the geom_point() function
map <- map + geom_point(data=locations, aes(x=lon, y=lat), color='green', size=2)

# Heatmap style visualization of density with countour lines
map <- map + stat_density2d(data=locations, aes(x=lon,y=lat, fill = ..level.., alpha = ..level..), geom='polygon', size=.3) + 
  scale_fill_gradient(low='yellow', high='red', guide=F) +
  stat_density2d(data=locations, aes(x=lon, y=lat), bins=5, color='red', size=.3) + 
  scale_alpha(range=c(0, .2), guide=F)

# Finally, we can annotate our plot

map <- map + ggtitle('Instagram locations in Helsinki') + geom_text(data=locations, aes(x=lon, y=lat, label=name), size=5, check_overlap=T)

# Type "map" to the console again to see your final map.
# Alternatively you can save your plot
png('my_plot.png',height=500,width=500,units='px')
map
dev.off()

###################################
# Exploring the data             #
###################################

# Total number of photos
nrow(photos)

# Total number of unique users posting photos in these locations
length(unique(photos$username))

# Summarizing data by location
# Ceck out also count(), join() and merge() functions!
locations['user_count'] <- NA
locations['photo_count'] <- NA
# sapply() summarizes users by applying the length() function for all location_ids (i.e. what is the length of the list of users for a location?)
locations['user_count'] <- sapply(locations$id, function(x) length(unique(photos[photos$location_id==x,]$username)))
# Again, we answer to the question "How many rows do we have after truncating our photos data frame to the specific location?" with sapply()
locations['photo_count'] <- sapply(locations$id, function(x) nrow(photos[photos$location_id==x,]))

# Draw histograms to see how popularity of places is distributed

# Histogram of user counts by location
hist(locations$user_count)
# Histogram of uploaded photos for each location
hist(locations$photo_count)

# Extract top 20 places with most users
plot_data <- locations[order(-locations$user_count),][1:20,]
plot_data <- transform(plot_data[,c('name','user_count')], name = reorder(name, order(user_count, decreasing=T)))

# Create a bar plot of user counts for the 20 most visiteg locations
ggplot(plot_data, aes(x=name, y=user_count)) + geom_bar(stat='identity') + theme_bw() + theme(axis.text.x=element_text(angle=90), axis.title.x=element_blank()) + ylab('User counts')

###################################
# Statistical tests               #
###################################

# Let's drop those photos with 0 tagged users and 0 likes
subset <- photos[photos$tagged_users > 0 & photos$likes > 0,]

# Since we're about to build a linear regression model, let's do a dummy normality check
hist(subset$likes)

# Log transform like counts since they're not normally distributed
likes <- log10(subset$likes)
tagged_users <- subset$tagged_users

# Check histogram of the log transformed data
hist(likes)

# Build simple linear regression
reg <- lm(likes ~ tagged_users)
plot(tagged_users, likes)
abline(reg, col='red')

# Check the summary to see if the relationship is statistically significant
summary(reg)

###################################
#  Upload intensity               #
###################################
# Extract the Day of Week from the timestamp
days <- format(as.Date(photos$created_at), format='%A')

# Calculate frequencies using the count() function from the plyr package
freq_table <- count(days)

ggplot(freq_table, aes(x=x, y=freq)) + geom_bar(stat='identity')  + theme_bw() + xlab('Day of week') + ylab('Photos uploaded') + ggtitle('Totel number of photos over a week')

###################################
#  Generate a wordcloud           #
###################################
# Let's count the occurances of each hashtag with the count() function
hashtag_freq <- count(hashtags)

# We can also rename the columns
names(hashtag_freq) <- c("hashtag","freq")

# Finally, let's generate a wordcloud. 
wordcloud(words=hashtag_freq$hashtag, freq=sqrt(hashtag_freq$freq), min.freq=1, max.words=200, rot.per=0.25,colors=brewer.pal(8,"Dark2"))

# Hint: type ?wordcloud in the console if you're using RStudio to see what additional parameters you can use to control the appearance of your wordcloud.