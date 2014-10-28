# !env Python
# Michael Herrera
# 10/18/14
# HW2, Problems 4 & 6
'''
Create a class to read discharge data for the Brazos river from this page:
Store date (as an array of datetime objects) and discharge data (an array of floating point
numbers, converted to cubic meters per second) as attributes within the class.

Create methods to:

 - Extract a year of discharge data. Return dates and discharges for the specified year.
 - Plot the hydrograph over the entire length of the timeseries.
 - Get a mean annual timeseries. Return the mean annual hydrograph with dates given for some arbitrary (specified) year.
 - Create a plot of a given year with mean discharge and variability. Plot the given year as a red line. Plot the annual mean hydrograph as a black line. Plot a grey shaded region around the black line representing one standard deviation about the mean (use the plt.fill() command for this).
'''
import numpy as np
import datetime
import matplotlib.pyplot as plt

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

if __name__ == '__main__':
    bd = Brazos('brazos_discharge.dat')
    years,dcs = bd.year_data(1998)
    savename = 'Full_Time_Series.pdf'
    bd.plot_all(savename)
    print "\nPlot for problem 4 has been saved as "+savename+"\n"

    year = 2012
    savename = 'Mean_Annual_Discharge_'+str(year)+'.pdf'
    bd = Brazos('brazos_discharge.dat')
    years,dcs = bd.year_data(year)
    mean_data, std_data = bd.get_series(year)
    bd.plot_series(years,mean_data,dcs,std_data,savename)
    print "\nPlot for problem 6 has been saved as "+savename+"\n"



