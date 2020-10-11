import gmplot
import pandas as pd
coordinates = pd.read_csv('coordination.csv')
gmap = gmplot.GoogleMapPlotter(40.721643, -74.070558, 30, apikey='AIzaSyD7k0YLCtod0NTuxmBMej0Cf70LdCzZSx4')
gmap.heatmap(coordinates.lat, coordinates.lon)#

gmap.scatter(coordinates.lat, coordinates.lon, c='r', marker=False, alpha = 0.1, size = 14)
gmap.draw('GMDensityFlask.html')

