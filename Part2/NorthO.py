# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:02:18 2017

@author: tanner
"""
pyplot.figure(figsize=(12,12))

import urllib2
import json
from mpl_toolkits.basemap import Basemap
import numpy 
import matplotlib.pyplot as pyplot

# lon_0, lat_0 are the center point of the projection.
# resolution = 'l' means use low resolution coastlines.
m = Basemap(projection='ortho',lon_0=-105,lat_0=40,resolution='l')
#m.drawcoastlines()
#m.fillcontinents(color='tan',lake_color='aqua')
# draw parallels and meridians.
#m.drawparallels(numpy.arange(-90.,120.,30.))
#m.drawmeridians(numpy.arange(0.,420.,60.))
#m.drawmapboundary(fill_color='aqua')
pyplot.title("WindNinja Launches in the Western Hemisphere")
#m.drawcountries()
m.bluemarble()

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
    m.plot(nn,mm,'ro',markersize=f[i],alpha=0.15)
    
    n.append(nn)
    q.append(mm)

pyplot.savefig('/home/tanner/src/wnUserMap/NorthAmericaTanRed',dpi=300,bbox_inches='tight')   
pyplot.show()

