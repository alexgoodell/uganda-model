
# ---------------------------  Mapping functions ------------------------

# - Created Mar 22, 2018 2:15 PM
# - Using tutorial: goo.gl/d8omVq
#
#
#
#
#
#


# ---------------------------  Mapping functions ------------------------

# Import dependencies
# requires pip install https://github.com/matplotlib/basemap/archive/master.zip

from lxml import etree
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib
from matplotlib.colors import Normalize
from matplotlib.collections import PatchCollection
from mpl_toolkits.basemap import Basemap
from shapely.geometry import Point, Polygon, MultiPoint, MultiPolygon
from shapely.prepared import prep
from pysal.esda.mapclassify import Natural_Breaks as nb
from descartes import PolygonPatch
import fiona
from itertools import chain

import config


# ---------------------------- Functions  -----------------------------------

# Convenience functions for working with colour ramps and bars
def colorbar_index(ncolors, cmap, labels=None, **kwargs):
    """
    This is a convenience function to stop you making off-by-one errors
    Takes a standard colour ramp, and discretizes it,
    then draws a colour bar with correctly aligned labels
    """
    cmap = cmap_discretize(cmap, ncolors)
    mappable = cm.ScalarMappable(cmap=cmap)
    mappable.set_array([])
    mappable.set_clim(-0.5, ncolors+0.5)
    colorbar = plt.colorbar(mappable, **kwargs)
    colorbar.set_ticks(np.linspace(0, ncolors, ncolors))
    colorbar.set_ticklabels(range(ncolors))
    if labels:
        colorbar.set_ticklabels(labels)
    return colorbar


def cmap_discretize(cmap, N):
    """
    Return a discrete colormap from the continuous colormap cmap.

        cmap: colormap instance, eg. cm.jet. 
        N: number of colors.

    Example
        x = resize(arange(100), (5,100))
        djet = cmap_discretize(cm.jet, 5)
        imshow(x, cmap=djet)

    """
    if type(cmap) == str:
        cmap = get_cmap(cmap)
    colors_i = np.concatenate((np.linspace(0, 1., N), (0., 0., 0., 0.)))
    colors_rgba = cmap(colors_i)
    indices = np.linspace(0, 1., N + 1)
    cdict = {}
    for ki, key in enumerate(('red', 'green', 'blue')):
        cdict[key] = [(indices[i], colors_rgba[i - 1, ki], colors_rgba[i, ki]) for i in xrange(N + 1)]
    return matplotlib.colors.LinearSegmentedColormap(cmap.name + "_%d" % N, cdict, 1024)


def cloro(v):

	# open shape file
	shp = fiona.open(config.data_path + '/gis/District_Boundaries_2014/District_Boundaries_2014.shp')
	bds = shp.bounds
	shp.close()
	# Calculate the extent, width and height of our basemap
	extra = 0.01
	ll = (bds[0], bds[1])
	ur = (bds[2], bds[3])
	coords = list(chain(ll, ur))
	w, h = coords[2] - coords[0], coords[3] - coords[1]

	# create Basemap instance
	m = Basemap(
	    projection='tmerc',
	    lon_0=-2.,
	    lat_0=49.,
	    ellps = 'WGS84',
	    epsg=5520,
	    llcrnrlon=coords[0] - extra * w,
	    llcrnrlat=coords[1] - extra + 0.01 * h,
	    urcrnrlon=coords[2] + extra * w,
	    urcrnrlat=coords[3] + extra + 0.01 * h,
	    lat_ts=0,
	    resolution='i',
	    suppress_ticks=True)
	m.readshapefile(
	    config.data_path + '/gis/District_Boundaries_2014/District_Boundaries_2014',
	    'uganda',
	    color='none',
	    zorder=2)

	df_map = pd.DataFrame({
	    'poly': [Polygon(xy) for xy in m.uganda if len(xy) > 2],
	    'district_name': [d[v] for d in m.uganda_info],
	    'pop': [d[v] for d in m.uganda_info]
	})

	# Calculate Jenks natural breaks for density
	breaks = nb(
	    df_map[df_map['pop'].notnull()]['pop'].values,
	    initial=300,
	    k=5)

	# the notnull method lets us match indices when joining
	jb = pd.DataFrame({'jenks_bins': breaks.yb}, index=df_map[df_map['pop'].notnull()].index)
	df_map = df_map.join(jb)
	df_map.jenks_bins.fillna(-1, inplace=True)

	# labels
	jenks_labels = ["<= %0.1f/km$^2$(%s wards)" % (b, c) for b, c in zip(
	    breaks.bins, breaks.counts)]
	jenks_labels.insert(0, 'No plaques (%s wards)' % len(df_map[df_map['pop'].isnull()]))

	plt.clf()
	fig = plt.figure(figsize=(10,10))
	ax = fig.add_subplot(111, frame_on=False)  

	# use a blue colour ramp - we'll be converting it to a map using cmap()
	cmap = plt.get_cmap('Blues')
	# draw wards with grey outlines
	df_map['patches'] = df_map['poly'].map(lambda x: PolygonPatch(x, ec='#555555', lw=0.1, alpha=1.0, zorder=0, aa=True))
	pc = PatchCollection(df_map['patches'], match_original=True)
	# impose our colour map onto the patch collection
	norm = Normalize()
	pc.set_facecolor(cmap(norm(df_map['jenks_bins'].values)))
	pc.set_alpha(0.8)
	ax.add_collection(pc)

	# Add a colour bar
	cb = colorbar_index(ncolors=len(jenks_labels), cmap=cmap, shrink=0.5, labels=jenks_labels)
	cb.ax.tick_params(labelsize=6)

	# Bin method, copyright and source data info
	smallprint = ax.text(
	    1.03, 0,
	    'Classification method: natural breaks\nContains Ordnance Survey data\n$\copyright$ Crown copyright and database right 2013\nPlaque data from http://openplaques.org',
	    ha='right', va='bottom',
	    size=4,
	    color='#555555',
	    transform=ax.transAxes)

	# Draw a map scale
	m.drawmapscale(
	    coords[0] + 0.08, coords[1] + 0.015,
	    coords[0], coords[1],
	    10.,
	    barstyle='fancy', labelstyle='simple',
	    fillcolor1='w', fillcolor2='#555555',
	    fontcolor='#555555',
	    zorder=5)

	m.drawcountries()
	plt.show()




# required to use as module
if __name__ == '__main__': 
	print "hello world"






