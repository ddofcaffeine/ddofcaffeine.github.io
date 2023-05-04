# -*- coding: utf-8 -*-
"""
Created on Thu May  4 18:11:29 2023

@author: bastd
"""

import pandas as pd
import folium
#import geopandas as gpd

#load data
file = "visited_cafes.xlsx"

data = pd.read_excel(file)

#remove the elements without coordinates
data = data.dropna(subset=['Coordinates'])

#prepare the coordinates
data['Coordinates'] = data['Coordinates'].map(lambda string: string.replace("\xa0", ""))
data['Coordinates'] = data['Coordinates'].map(lambda string: string.split(", "))

#Change the type of the rating to string
data['Rating'] = data['Rating'].map(lambda element: str(element))
#add the rating scale
data['Rating'] = data['Rating'] + "/5"

#format the comments
data['Comments'] = data['Comments'].map(lambda string: string.replace('"', ""))
data['Comments'] = data['Comments'].map(lambda string: string.replace("+", '<br> + '))

#create the map
cafesMap = folium.Map(location = [49.986242683299984, 15.868388651351117], tiles = "OpenStreetMap", zoom_start = 5)

for i in range(len(data['Comments'])):
    name = data['Name'][i]
    rating = data['Rating'][i]
    description = data['Comments'][i]
    link = data['Weblinks'][i]
    cafesMap.add_child(folium.Marker(location = data['Coordinates'][i], icon= folium.Icon(color="lightred", icon = 'mug-hot', prefix = 'fa'), popup = "<b>" + name + "</b>" + "<br>" + "<br>" 
                                    + rating + "<br>" + description + "<br>" + "<br>" + '<a href="' + link + 'target="_blank">' + link + '</a>'))
    
    
cafesMap.save("map.html")