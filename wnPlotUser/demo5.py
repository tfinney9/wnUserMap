# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:40:23 2017

@author: tanner
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='ortho',llcrnrlat=20,urcrnrlat=50,\
            llcrnrlon=-130,urcrnrlon=-60,resolution='c')
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.fillcontinents(color='#04BAE3', lake_color='#FFFFFF')
m.drawmapboundary(fill_color='#FFFFFF')

lat = 30
lon = -103


lat2 = 40,33,44,31,30
lon2 = -113,-100,-102,-111,-112

x,y = m(lon,lat)
m.plot(x,y,'ro',markersize=20,alpha=.5)

#x,y = m(lon2,lat2)
#m.plot(x,y,'go',markersize=20,alpha=.5)

plt.title('Geo Plotting')
plt.show()