# !env python
# Michael Herrera
# 10/17/14
# HW1, Problem 3
#
# Write a function to read the data from the file discharge.dat,
# return a list of dates (as datetime objects) and discharge.

import datetime

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

if __name__ == '__main__':
    filename = 'discharge.dat'
    date,discharge = read_dat(filename)

    print 'Problem 3:'
    print '   Date      Discharge(ft^3/s)'
    for i in range(10):
        print date[i],'       ',discharge[i]






