import numpy as np
import datetime

def fib(n):
	""" 
	Writes out the Fibonacci Sequence to n numbers
	Inputs:
		n = Number of numbers in sequence
	Outputs:
		fibnums = Fibonacci sequence to n numbers 
	"""
	fibnums = [0]
	for i in range(0,n):
		if (i==0):
			fibnums.append(1)
		else:
			fn1 = fibnums[i]
			fn2 = fibnums[i-1]
			fibnums.append(fn1+fn2)
	
	return fibnums[1:]

def integrate(f,dx=1.0):
	"""
	Computes the integral of a list of numbers using the trapezoidal rule
	Inputs
		f  = List of values in function
		dx = Grid spacing, default of 1.0
	Output
		var =  Integral of function
	"""
	if (len(f) >2 ):
		var = (dx/2.0)*(f[0]+2*sum(f[1:-1])+f[-1])
	else:
		var = (dx/2.0)*(sum(f))
	return var	

def read_dat(filename):
	"""
	Reads a discharge file skipping the header information.
	Returns the datetime object and discharge for the date.
	Inputs:
		filename = Name of the input file
	Outputs:
		dt = Datetime object
		dc = Discharge rate
	"""
	f = open(filename,'r')
	dt_form = '%Y-%m-%d'
	dt = []
	dc = []
	for line in f.readlines():	
		if (line[0] != '#'):
			temp = line.split('\t')
			dt.append(datetime.datetime.strptime(temp[2],dt_form).date())
			dc.append(temp[3].split('_')[0])
	f.close()
	return dt,dc

def read_drifter(filename):
	"""
	Read in drifter file and stores the position data for each track.
	Inputs:
		filename = Name of the input file
	Outputs:
		data = Dictionary containing lat,lon data for each track.  
	"""		
	f = open(filename,'r')
	data = {}
	keys = []
	
	for line in f.readlines():
		temp = line.split('\t')
		if (temp[0] == 'Track'):
			name = temp[1]
			latlon = []
		elif (temp[0] == 'Trackpoint'):
			coords = temp[1].split()
			if (coords[0][0] == 'N'):
				hemi1 = 1
			else:
				hemi1 = -1
			if (coords[2][0] == 'E'):
				hemi2 = 1
			else:
				hemi2 = -1
			lat = hemi1*(int(coords[0][1:]) + float(coords[1])/60.0)
			lon = hemi2*(int(coords[2][1:]) + float(coords[3])/60.0)
			lat = "%.3f" % lat
			lon = "%.3f" % lon
			latlon.append((lat,lon))
			data.update({name:latlon})	

	f.close()
	return data



