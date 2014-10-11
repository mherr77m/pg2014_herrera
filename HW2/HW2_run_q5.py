# Michael Herrera
# Homework 2 Run Script for Problem 5
# OCNG 689

import HW2_mod as hw

# Problem 5
# Create a function to read in topography/bathymetry data and plot it. 

filename = 'global_merged5.txt'
savename = 'Topo_Bath.png'

hw.plot_topo(filename,savename)

print "\nPlot for problem 5 has been saved as "+savename+"\n"





