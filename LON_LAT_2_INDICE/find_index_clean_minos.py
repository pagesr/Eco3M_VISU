

################################################################################################################
# Vizu des donnees dyfamed et comparaison avec le model
# Remi Pages 25/04/2017
# Mise a jour le 5/05/2019 pour MED8
###############################################################################################################

from tempfile import TemporaryFile
import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt 
from netcdftime import utime
import os
from matplotlib import lines
from matplotlib.lines import Line2D
from itertools import cycle
from netcdftime import utime
from pylab import figure
import pandas as pd
import matplotlib.patches as mpatches
eco = Dataset("/home/remi/Documents/THESE/POST_PROCESSING/MED8/VALIDATION/TMP/1990_diag.nc") 
time=eco.variables['time_counter']          
lon = eco.variables['nav_lon']
lat = eco.variables['nav_lat']
lon=np.array(lon)
lat=np.array(lat)
chl=eco.variables['CHL_TOT']
k=0
o=0
lonlatmod=lon+lat
index=pd.read_csv('lonlat_minos.csv',delim_whitespace=True,skiprows=1,header=None)
index=np.array(index)
lonlatmod=np.abs(lonlatmod[:])
#~~~~~~~~ POUR AUTRE QUE BOUM ~~~~~~~~~~~~~~~~~~~~~~
longitude=index[:,2]
latitude=index[:,1]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
lonlat=longitude+latitude
lonmod=np.zeros(shape=(2,20))
latmod=np.zeros(shape=(2,20))
#---------------------------------------------------


for m in range(0,20):  # nb de station  
	for j in range (0,160-1):
		for i in range (0,394-1):

			if lat[j,i]<latitude[m] and lat[j+1,i]>latitude[m] :
			#	print '------------------------------------------------'
			#	print  lat[j,i], latitude[m],  lat[j,i+1]
				if lon[j,i]<longitude[m] :
					#print 'm2',m
					if lon[j,i+1]>longitude[m]:
						latmod[0,m]=i
						latmod[1,m]=j
						print 'm3', m
				#		print i, j, lon[j,i], longitude[m], lat[j,i], latitude[m]
#						print 'OK OKOKOKOKOKOKOKOKOKOKOKOKOKO
# CORRECTION 
for i in range(0,len(latmod[0,:])):
	if latmod[0,i]== 0.0:
		latmod[0,i]=int((latmod[0,i-1]+latmod[0,i+1])/2)
	if latmod[1,i]== 0.0:
		latmod[1,i]=int((latmod[1,i-1]+latmod[1,i+1])/2)



plt.imshow(chl[0,0,:,:],origin='lower')
plt.plot(latmod[0,:],latmod[1,:],'r+')
plt.show()

np.savetxt('minos_i.out', latmod[0,:], delimiter=',')
np.savetxt('minos_j.out', latmod[1,:], delimiter=',')


