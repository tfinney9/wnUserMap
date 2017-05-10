# -*- coding: utf-8 -*-
"""
Created on Wed May 10 09:27:58 2017

@author: tanner
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap
import numpy as np

plt.figure(figsize=(12,12))

map = Basemap()

fig = plt.figure()
ax = Axes3D(fig)


ax.azim = 250
ax.elev = 50
ax.dist = 9


ax.add_collection3d(map.drawcoastlines(linewidth=0.25))
ax.add_collection3d(map.drawcountries(linewidth=0.35))

lons = np.array([-13.7, -10.8, -13.2, -96.8, -7.99, 7.5, -17.3, -3.7])
lats = np.array([9.6, 6.3, 8.5, 32.7, 12.5, 8.9, 14.7, 40.39])
cases = np.array([1971, 7069, 6073, 4, 6, 20, 1, 1])
deaths = np.array([1192, 2964, 1250, 1, 5, 8, 0, 0])
places = np.array(['Guinea', 'Liberia', 'Sierra Leone','United States', 'Mali', 'Nigeria', 'Senegal', 'Spain'])

x, y = map(lons, lats)

ax.bar3d(x, y, np.zeros(len(x)), 2, 2, deaths, color= 'r', alpha=0.8)




plt.show()
