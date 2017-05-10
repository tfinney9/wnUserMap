# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:05:57 2017

@author: tanner
"""

import urllib2
import json
from mpl_toolkits.basemap import Basemap
import numpy
import matplotlib.pyplot as pyplot

pyplot.figure(figsize=(12,12))

# setup albers equal area conic basemap
# lat_1 is first standard parallel.
# lat_2 is second standard parallel.
# lon_0,lat_0 is central point.
m = Basemap(width=8000000,height=7000000,
            resolution='l',projection='aea',\
            lat_1=40.,lat_2=60,lon_0=35,lat_0=50)
#m.bluemarble()
m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(numpy.arange(-80.,81.,20.))
m.drawmeridians(numpy.arange(-180.,181.,20.))
m.drawmapboundary(fill_color='aqua')
# draw tissot's indicatrix to show distortion.
ax = pyplot.gca()
#for y in numpy.linspace(m.ymax/20,19*m.ymax/20,10):
#    for x in numpy.linspace(m.xmax/20,19*m.xmax/20,12):
#        lon, lat = m(x,y,inverse=True)
#        poly = m.tissot(lon,lat,1.25,100,\
#                        facecolor='green',zorder=10,alpha=0.5)
pyplot.title("WindNinja Launches in Europe, the Middle East and North Africa")
url='http://windninja.org:34333/user'

def readData(url):
    new=urllib2.urlopen(url)
    response=new.read()
    json_string=response
    a=json.loads(json_string)
    return a
    
xx=-3.68
xy=40.4
q=[]
n=[]

response=readData(url)

size=numpy.arange(50,1,-1)

for i in range(len(response)):
    a=response[i]['x']
    b=response[i]['y']
    nn,mm=m(a,b)
    af=numpy.ones(len(response)-len(size))
    af=af*3
    f=numpy.append(size,af)
    m.plot(nn,mm,'bo',markersize=f[i],alpha=0.35)
    
    n.append(nn)
    q.append(mm)
    
#    m.plot(n,q,'bo',markersize=3,alpha=1)

pyplot.savefig('/home/tanner/src/wnUserMap/EuropeAlbersCoralBordersBlue',dpi=300,bbox_inches='tight')
pyplot.show()