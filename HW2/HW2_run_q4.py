# Michael Herrera
# Homework 2 Run Script for Problem 4
# OCNG 689

import HW2_mod as hw

# Problem 4
# Create a class to read in discharge data and retrieve 
# date and discharge data from the file.

bd = hw.Brazos('brazos_discharge.dat')
years,dcs = bd.year_data(1998)
savename = 'Full_Time_Series.pdf'
bd.plot_all(savename)
print "\nPlot for problem 4 has been saved as "+savename+"\n"
