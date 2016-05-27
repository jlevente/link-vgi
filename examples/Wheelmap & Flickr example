Step 1:		Add the .csv files to QGIS, selecting WGS84 as the coordinate system
Step 2:		Create Voronoi Polygons for the Wheelmap dataset (Vector->Geometry tools->Voronoi polygons)
Step 3:		perform a heatmap analysis on the Flickr dataset (Raster->Heatmap->Heatmap...), setting the distance to be 20m (you can play around with this to get different results for clustering)
Step 4:		Use the raster calculator (Raster->Raster calculator) to create a raster showing only the area with 3 or more images within the distance value set in the previous step. ([heatmap_layer] >= 3)
Step 5:		Convert the raster to a polygon (Raster->Conversion->Polygonise)
Step 6:		Filter the resulting polygon shapefile to only show the areas with 3 or more images (Right-click layer->Filter, "DM"==1)
Step 7:		Generate centroid points for these polygons (Vector->Geometry Tools->Polygon Centroids)
Step 8:		Perform an attribute join (Vector->Data Management->Join attributes by location) with the target layer as the centroids and the join layer as the voronoi polygons
