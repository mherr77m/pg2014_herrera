# !env Python
# Michael Herrera
# 10/18/14
# HW2, Problem 5
'''
Write a function to read the topography/bathymetry of the world using the ETOPO5 surface dataset:

http://www.nio.org/userfiles/file/datainfo/global_merged5.txt

and return three arrays representing x, y, and z. Write a script using this function to make a pcolormesh map of the topo/bathy, and overlay the contours z = [-1000, 0, 1000]. The negative contour should be thin and dashed, the 0 contour thick and solid, and the 1000 contour thin and solid.
'''
import numpy as np
import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def plot_topo(filename,savename):
    """
    Reads in the topography/bathemetry text file and plots the data.
    """
    f = open(filename,'r')

    lon=[]
    lat=[]
    topo=[]
    for line in f.readlines():
        temp = line.split()
        if (float(temp[0]) == -180.0):
            lat.append(float(temp[1]))
        if (float(temp[1]) == -90.0):
            lon.append(float(temp[0]))
        topo.append(float(temp[2]))

    topo = np.array(topo).reshape((len(lat),len(lon)))

    lons,lats = np.meshgrid(lon,lat)

    m = Basemap(projection='cyl',
                llcrnrlon=-180,
                urcrnrlon=180,
                llcrnrlat=-90,
                urcrnrlat=90)

    x,y = m(lons,lats)

    fig = plt.figure(figsize=(10,5))
    m.drawmeridians(np.arange(-180,181,30),labels=[1,0,0,1])
    m.drawparallels(np.arange(-90,91,30), labels=[0,1,1,0])

    pcm = m.pcolormesh(x,y,topo,cmap='RdBu_r',vmin=-6000,vmax=6000)
    m.contour(x,y,topo,[-1000,0,1000],colors='k',linewidths=[.5, 1, .5])
    
    cax = fig.add_axes([0.68, 0.17, 0.14, 0.02])
    cb = plt.colorbar(pcm, cax=cax, orientation='horizontal',ticks=[-6000,-3000,0,3000,6000])
    cb.set_label('Topography/Bathymetry [m]',fontsize=6)
    xtl = cax.get_xticklabels()
    for foo in xtl:
        foo.set_fontsize(6)
    plt.savefig(savename,dpi=600)

if __name__ == '__main__':
    filename = 'global_merged5.txt'
    savename = 'Topo_Bath.png'
    plot_topo(filename,savename)
    print "\nPlot for problem 5 has been saved as "+savename+"\n"
