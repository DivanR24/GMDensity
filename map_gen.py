import os
import gmplot
import pandas as pd
import webbrowser
import requests

def fetch_map():
  # query the api
  self_la = 0
  self_ln = 0
  url = 'http://api.ipstack.com/check?access_key=11677f348c7d10f099411e1ba2437f48'
  r = requests.get(url)
  d = r.json()

  self_la = d['latitude']
  self_ln = d['longitude']

  coordinates = pd.read_csv('coordination.csv')
  
  print(self_la, self_ln)
  print(coordinates.tail())
  
  # gmap = gmplot.GoogleMapPlotter(40.721643, -74.070558, 16, apikey='AIzaSyD7k0YLCtod0NTuxmBMej0Cf70LdCzZSx4')
  gmap = gmplot.GoogleMapPlotter(self_la, self_ln, 16, apikey='AIzaSyD7k0YLCtod0NTuxmBMej0Cf70LdCzZSx4')
  
  # self_lat, self_lng = zip(*[(self_la, self_ln), (0, 0) ])

  # gmap.scatter(x, y, c="r", marker = True, size=100,color='cornflowerblue')

  # plots the sample points
  gmap.heatmap(coordinates.lat, coordinates.lon)
  gmap.scatter(coordinates.lat, coordinates.lon, c='r', marker=False, alpha = 0.1, size = 14)
  
  # plots the user's location
  gmap.scatter([self_la], [self_ln], c='b', marker=False, size = 20)
  gmap.draw('templates/index.html')
  gmap.draw('index.html')

if __name__ == '__main__':
  webbrowser.open(os.path.join(os.path.dirname(__file__) + '/templates/' + 'index.html'))
