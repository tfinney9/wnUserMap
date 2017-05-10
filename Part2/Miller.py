# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:10:28 2017

@author: tanner
"""
#plt.figure(figsize=(12,12))


from mpl_toolkits.basemap import Basemap
import numpy
import matplotlib.pyplot as pyplot
# lon_0 is central longitude of projection.
# resolution = 'c' means use crude resolution coastlines.
m = Basemap(projection='kav7',lon_0=0,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(numpy.arange(-90.,120.,30.))
m.drawmeridians(numpy.arange(0.,360.,60.))
m.drawmapboundary(fill_color='aqua')
pyplot.title("Test1")
pyplot.show()