import pandas as pd 
import numpy as np 
import folium

data = pd.read_csv("events_Barcelona.csv") 
data = data.drop(data.columns[4:8],axis=1)
data = data.dropna()
data = data[data.coordinates0 != 'None']
data = data[data.coordinates0 != '0']

def strtoint(x):
	for index,row in data.iterrows():
		try:
			return float(x)
		except ValueError:
		return 0

data['coordinates0'] = data['coordinates0'].apply(strtoint)
data['coordinates2'] = data['coordinates2'].apply(strtoint)

locations = data[['coordinates0', 'coordinates2']]
locationlist = locations.values.tolist()

m = folium.Map(location=[41.38, 2.17],tiles='CartoDB dark_matter', zoom_start=12)

for point in range(0, len(locationlist)):
    m.add_child(folium.Marker(locationlist[point], popup=folium.Popup(data.Event)))
    
m
