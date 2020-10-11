import gmplot
def mapgenerator():
  gmap = gmplot.GoogleMapPlotter.from_geocode('Jersey City', )
  gmap.heatmap()
  gmap.scatter()
  gmap.draw()
print("Hello World.")