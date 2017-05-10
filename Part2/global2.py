# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:14:52 2017

@author: tanner
"""

import numpy
import urllib2
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pyplot
import datetime

pyplot.figure(figsize=(12,12))

url='http://windninja.org:34333/user'

def readData(url):
    new=urllib2.urlopen(url)
    response=new.read()
    json_string=response
    a=json.loads(json_string)
    return a

#response = readData(url)


from mpl_toolkits.basemap import Basemap

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


x,y=m(xx,xy)

now=datetime.datetime.now()
t="Last updated at: "+str(now)

pyplot.title(t)
pyplot.savefig('/home/tanner/src/wnUserMap/Global2',dpi=300,bbox_inches='tight')   
pyplot.show()


