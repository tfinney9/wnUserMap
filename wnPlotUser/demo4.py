# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:31:12 2017

@author: tanner
"""

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
# create new figure, axes instances.
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
# setup mercator map projection.
#m = Basemap(llcrnrlon=-100.,llcrnrlat=20.,urcrnrlon=20.,urcrnrlat=60.,\
#            rsphere=(6378137.00,6356752.3142),\
#            resolution='l',projection='merc',\
#            lat_0=40.,lon_0=-20.,lat_ts=20.)

m=Basemap(projection='ortho',lat_0=50,lon_0=-50,resolution='l')

#            map = Basemap(projection='ortho',lat_0=45,lon_0=-100,resolution='l')

# nylat, nylon are lat/lon of New York
nylat = 40.78; nylon = -73.98
# lonlat, lonlon are lat/lon of London.
lonlat = 51.53; lonlon = 0.08
# draw great circle route between NY and London

x,y = m(nylon,nylat)
m.plot(x,y,'ro',markersize=20,alpha=0.5)
x2,y2=m(lonlon,lonlat)
m.plot(x2,y2,'go',markersize=20,alpha=0.5)
m.drawgreatcircle(nylon,nylat,lonlon,lonlat,linewidth=2,color='b')
m.drawcoastlines()
m.fillcontinents()
# draw parallels
m.drawparallels(np.arange(-90,90,20),labels=[1,1,0,1])
# draw meridians
m.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])
#ax.set_title('Great Circle from New York to London')
plt.show()