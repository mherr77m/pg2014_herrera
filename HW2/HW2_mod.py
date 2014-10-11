# Michael Herrera
# Functions for Homework 2
# OCNG 689

import numpy as np
import math
import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def distance(array1,array2):
    """
    Calculates the distance between all points in two
    arrays.  The arrays don't have to be the same size.
    Each array has the form [[x1,y1],[x2,y2],...,[xn,yn]]
    """
	
    # Use array broadcasting in the distance formula to 
    # allow for arrays of different sizes
    dist = np.sqrt((array1[:,0,np.newaxis] - array2[:,0])**2 + \
                   (array1[:,1,np.newaxis] - array2[:,1])**2)
    return dist

class Point(object):
    """
    Defines a Point object as a point in space.
    Attributes:
        x - x coordinate
        y - y coordinate
    Methods:
        distance - Calculates the distance between two
                   points.
        rotate - Rotates the point by a specified number
                 of radians around another point.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self,other):
        return Point(self.x-other.x, self.y-other.y)

    def __str__(self):
        return '(%.2f, %.2f)' % (self.x, self.y)

    def __repr__(self):
        return 'Point(%.2f, %.2f)' % (self.x, self.y)

    def distance(self, p=None):
        if p is None:
            p = Point(0.0, 0.0)
        
        return math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)

    def rotate(self, angle, p=None):
        if p is None:
            p = Point(0.0, 0.0)

        p_temp = self - p
        self.x = p.x + p_temp.x * math.cos(-angle) - \
                 p_temp.y * math.sin(-angle)
        self.y = p.y + p_temp.x * math.sin(-angle) + \
                 p_temp.y * math.cos(-angle)

def high_pass(x, y, n = 1):
    """
    High pass filter.  Takes x,y data as input and removes 
    the trend from the data based on a polynomial function
    of the given order, default is linear.
    """
    psol = np.polynomial.Polynomial.fit(x, y, n)
    new_y = psol(x)
    return y - new_y

class Brazos(object):
    """
    Attributes:
        dates - An array of the dates for the data in the file
        dc - An array of the discharge rates for the dates
    Methods:
        year_data(year) - Retrieves the dates and discharge rates
                          for a given year.
        plot_all() - Plots all of the discharge data from the file.
        get_series(year) - Given a year, retrieves an average discharge
                           rate and standard deviation for each date in 
                           that year over the whole file.
        plot_series(dates, mean_series, year_series, std_series) - Plots
                           the mean discharge rate, the discharge rate
                           for the given year, and the variance in the mean.
    """
    
    def __init__(self,filename):
        """
        Opens the file and reading the dates and discharges for the 
        entire file.  It also masks the missing values.
        """
        f = open(filename,'r')
        dates = []
        dc = []
        dt_form = '%Y-%m-%d'
        for line in f.readlines():
            temp = line.split('\t')
            if (temp[0] == 'USGS'):
                dates.append(datetime.datetime.strptime(temp[2],\
                             dt_form).date())
                try:
                    dc.append(int(temp[3])*0.0283168466)
                except ValueError:
                    dc.append(-9999)
        self.dc = np.ma.masked_where(np.array(dc) == -9999, np.array(dc))
        self.dates = np.array(dates)

    def year_data(self,year):
        """
        Retrieves a single year of dates and discharge data.  The method
        first retrieves the index for the data in the year and then 
        returns the data for the corresponding indicies.
        """
        idx = [i for i in range(self.dates.shape[0]) if self.dates[i].year == year]
        year_dates = self.dates[idx]
        year_dc = self.dc[idx]
        return year_dates, year_dc

    def plot_all(self,savename):
        """
        Plots the entire file.
        """
        fig = plt.figure(figsize=(10,3))
        ax = fig.gca()
        ax.plot(self.dates,self.dc,'k')
        ax.set_ylabel('$m^3/s$')
        ax.set_title('Brazos River Discharge Near Rosharon, TX')
        ax.set_aspect('equal')
        plt.savefig(savename)

    def get_series(self,year):
        """
        Retrieves the data for a single year and then calculates
        the annual mean for the dates in the given year and the 
        standard deviation.  
        """
        year_dates, year_dc = self.year_data(year)
        mean_dc = []
        std_dc = []
        for date in year_dates:
            day = date.day
            month = date.month
            idx = [i for i in range(self.dates.shape[0]) \
                   if (self.dates[i].month == month and \
                       self.dates[i].day == day)]
            mean_dc.append(np.ma.mean(self.dc[idx]))
            std_dc.append(np.ma.std(self.dc[idx]))

        return np.array(mean_dc), np.array(std_dc)

    def plot_series(self, dates, mean_series, year_series, std_series, savename):
        """
        Plots the annual mean discharge with the variance and the discharge
        from the given year.
        """
        year = dates[0].year
        year_label = 'Discharge for '+str(year)
        dates2 = np.concatenate([dates,dates[::-1]])
        std2 = np.concatenate([std_series+mean_series,\
                              (mean_series-std_series)[::-1]])
        fig = plt.figure(figsize=(10,5))
        ax = fig.add_subplot(111)
        p1 = ax.plot(dates,mean_series,'-k', label = 'Mean Discharge')
        p3 = ax.fill(dates2,std2,facecolor = 'gray',label='Mean Variance')
        p2 = ax.plot(dates,year_series,'-r', label = year_label)
        ax.set_ylabel('$m^3/s$')
        ax.set_title('Brazos River Discharge Near Rosharon, TX')
        plt.ylim([0,max(year_series)+500])
        plt.legend(fontsize='x-small')
        idx = [i for i in range(dates.shape[0]) if (dates[i].day == 1)]
        dt_form = '%b'
        plt.xticks(dates[idx],[datetime.datetime.strftime(dates[i],dt_form) for i in idx])
        plt.savefig(savename)

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

