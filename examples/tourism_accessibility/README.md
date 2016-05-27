The purpose of this exercise is to assess the accessibility of popular locations based on data from Flickr and Wheelmap. It is far from a perfect approach and is simply an example of how you can use data from two sources to perform a simple piece of analyis.

Within this exercise, you will use images from Flickr as a proxy to popular locations, based on the assumption that areas with a high density of images taken there will be a popular location. These locations will then be given an accessibilty value based on the closest POI obtained from Wheelmap.

## Wheelmap
[Wheelmap](http://wheelmap.org) is a service developed by Soyialhelden in Berlin which aims at allowing users to view and edit whether a place is accessible to wheelchair users. The base data used are POI features from OSM, with the accessibilty information being stored agains the POI in the OSM dataset. The possible values for this accessibility are "yes", "limited", "no" and "unknown".

## Flickr
[Flickr](http://flickr.com) is a widely used platform for uploading and sharing photogrpahs. As many cameras and smartphones now include in built GPS technology, a number of these photographs are geotagged when they are taken. This information is then uploaded alongside the image and the images can be searched for by geographic location.

## Stages

Step 1:		Add the .csv files to QGIS, selecting WGS84 as the coordinate system

Step 2:		Create Voronoi Polygons for the Wheelmap dataset (Vector->Geometry tools->Voronoi polygons)

Step 3:		perform a heatmap analysis on the Flickr dataset (Raster->Heatmap->Heatmap...), setting the distance to be 20m (you can play around with this to get different results for clustering)

Step 4:		Use the raster calculator (Raster->Raster calculator) to create a raster showing only the area with 3 or more images within the distance value set in the previous step. ([heatmap_layer] >= 3)

Step 5:		Convert the raster to a polygon (Raster->Conversion->Polygonise)

Step 6:		Filter the resulting polygon shapefile to only show the areas with 3 or more images (Right-click layer->Filter, "DM"==1)

Step 7:		Generate centroid points for these polygons (Vector->Geometry Tools->Polygon Centroids)

Step 8:		Perform an attribute join (Vector->Data Management->Join attributes by location) with the target layer as the centroids and the join layer as the voronoi polygons
