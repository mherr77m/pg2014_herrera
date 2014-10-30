from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import netCDF4

nc=netCDF4.Dataset('http://apdrc.soest.hawaii.edu/dods/public_data/satellite_product/AVHRR/avhrr_clima')
m = Basemap(projection='lcc',
            llcrnrlon=-90, 
            urcrnrlon=120, 
            llcrnrlat=0, 
            urcrnrlat=60,
            lat_0=30.0,
            lon_0=-50,
            resolution='c') 
           
lon=nc.variables['lon'][:]
lat=nc.variables['lat'][:]
sst=nc.variables['sst'][0,:,:]

x,y = m(*np.meshgrid(lon,lat))
fig=plt.figure(figsize=(8,8))

m.fillcontinents()
pcm=plt.pcolormesh(x,y,sst,cmap=plt.cm.spring)
m.drawmeridians(np.arange(-180,121,20),labels=[1,0,0,1])
m.drawparallels(np.arange(0,91,20), labels=[0,1,1,0])
m.drawcountries()
cax = fig.add_axes([0.3, 0.85, 0.2, 0.02])
cb = plt.colorbar(pcm, cax=cax, orientation='horizontal',ticks=range(0,33,8))
cb.set_label('Sea Surface Temperature [C]',fontsize=8)

xtl = cax.get_xticklabels()

for foo in xtl:
    foo.set_fontsize(8)


plt.savefig('test.png')



