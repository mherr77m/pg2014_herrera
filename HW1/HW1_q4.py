# !env python
# Michael Herrera
# 10/17/14
# HW1, Problem 4
#
# Write a function to read data from the file drifter.dat.  
# Return a dictionary based on the track name as indices, 
# returning a list of lat/lon pairs

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

if __name__ == '__main__':
    filename = 'drifter.dat'
    tracks = read_drifter(filename)

    print 'Problem 4:'
    print 'tracks[''FRODO''] :',tracks['FRODO']
    print 'tracks[''STRIDER''] :',tracks['STRIDER']
    print 'tracks[''ACTIVE LOG 003''] :',tracks['ACTIVE LOG 003']
