# Michael Herrera
# Homework 2 Run Script for Problem 6
# OCNG 689

import HW2_mod as hw

# Problem 6
# Add methods to the class from problem 4 to calculate the
# mean annual hydrograph and the corresponding standard deviation,
# and plot the returned data.

year = 1998
savename = 'Mean_Annual_Discharge.pdf'

bd = hw.Brazos('brazos_discharge.dat')

years,dcs = bd.year_data(year)
mean_data, std_data = bd.get_series(year)

bd.plot_series(years,mean_data,dcs,std_data,savename)

print "\nPlot for problem 6 has been saved as "+savename+"\n"





