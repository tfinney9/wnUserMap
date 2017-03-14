# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 09:47:29 2017

@author: tanner
"""

import numpy
import urllib2
import json
import matplotlib.pyplot as pyplot
#import csv

count=[]
country=[]
region=[]

url='http://windninja.org:34333/report?fmt=json'

def readData(url):
    new=urllib2.urlopen(url)
    response=new.read()
    json_string=response
    a=json.loads(json_string)
    return a
    
response = readData(url)

print len(response)

for i in range(len(response)):
    count.append(response[i]['count'])
    country.append(response[i]['country'])
    region.append(response[i]['region'])
    
index=numpy.arange(len(country))

sCount=[]
sCountry=[]
sRegion=[]

plotRange=15

for i in range(plotRange):
#    if count[i]>10:
        sCount.append(count[i])
        sCountry.append(country[i])
        sRegion.append(region[i])


sIndex=numpy.arange(len(sCountry))

usa='United States'

sLoc=[]

for i in range(len(sCountry)):
    sArea=sCountry[i]+', '+sRegion[i]
    sLoc.append(sArea)

mCount=[]
mCountry=[]
mRegion=[]
secondRange=31
for i in numpy.arange(plotRange,secondRange):
    mCount.append(count[i])
    mCountry.append(country[i])
    mRegion.append(region[i])

mLoc=[]

for i in range(len(mCountry)):
    mArea=mCountry[i]+', '+mRegion[i]
    mLoc.append(mArea)

mIndex=numpy.arange(len(mCountry))

pyplot.figure(0)
pyplot.barh(sIndex,sCount,alpha=0.75,color='r',align='center')
pyplot.ylim(-1,plotRange)
pyplot.gca().invert_yaxis()
pyplot.yticks(sIndex,sLoc,size='small')
pyplot.xticks(rotation='45')
pyplot.grid(axis='x')
pyplot.title('WindNinja Launches By Country (top 15)')
pyplot.savefig('/home/tanner/output/umap/15.png',bbox_inches='tight',dpi=300)


pyplot.figure(1)
pyplot.barh(mIndex,mCount,alpha=0.75,color='purple',align='center')
pyplot.ylim(-1,plotRange)
pyplot.gca().invert_yaxis()
pyplot.yticks(mIndex,mLoc,size='small')
pyplot.xticks(rotation='45')
pyplot.grid(axis='x')
pyplot.title('WindNinja Launches By Country (15-30)')
pyplot.savefig('/home/tanner/output/umap/30.png',bbox_inches='tight',dpi=300)






