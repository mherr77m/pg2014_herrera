import numpy as np
import datetime

def fib(n):
	# Writes out the Fibonacci Sequence to n numbers
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
	# Computes the integral of a list of numbers using the trapezoidal rule
	if (len(f) >2 ):
		var = (dx/2.0)*(f[0]+2*sum(f[1:-1])+f[-1])
	else:
		var = (dx/2.0)*(sum(f))
	return var	

def read_dat(filename):
	# Reads a discharge file skipping the header information.
	# Returns the datetime object and discharge for the date.
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
	# Get each waypoint from the beginning of the file,
	# then reads through the file until it finds data for the waypoint.
	# Puts the lat, lon data into a dictionary for each waypoint key. 
	f = open(filename,'r')
	data = {}
	keys = []
	while True:
		line = f.readline()
		if not line: break
		temp = line.split('\t')
		if (temp[0] == 'Track'):
			flag = True
			latlon = []
			while True:
				line2 = f.readline()
				temp2 = line2.split('\t')
				if (temp2[0] == 'Trackpoint'):
					lat = temp2[1].split(' ')[1]
					lon = temp2[1].split(' ')[3]
					latlon.append((lat,lon))
					flag = False
				elif (flag == False): break
			data.update({temp[1]:latlon})
	f.close()
	return data




