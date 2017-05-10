# -*- coding: utf-8 -*-
"""
Created on Wed May 10 09:27:01 2017

@author: tanner
"""

plt.figure(figsize=(12,12))

import numpy
import urllib2
import json
import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap


url='http://windninja.org:34333/user'

def readData(url):
    new=urllib2.urlopen(url)
    response=new.read()
    json_string=response
    a=json.loads(json_string)
    return a

#response = readData(url)



# lon_0 is central longitude of projection.
# resolution = 'c' means use crude resolution coastlines.
m = Basemap(projection='kav7',lon_0=0,resolution='c')
#m.drawcoastlines()
#m.fillcontinents(color='tan',lake_color='aqua')
# draw parallels and meridians.
#m.drawparallels(numpy.arange(-90.,120.,30.))
#m.drawmeridians(numpy.arange(0.,360.,60.))
#m.drawmapboundary(fill_color='aqua')
#m.drawcountries()
m.bluemarble()

xx=-3.68
xy=40.4
q=[]
n=[]

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


x,y=m(xx,xy)




pyplot.title("WindNinja Global Launches")
#pyplot.savefig('/home/tanner/src/wnUserMap/GlobalBMRed',dpi=300,bbox_inches='tight')   
pyplot.show()