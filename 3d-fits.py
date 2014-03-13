## generate a 3D plot from a table of FITS values

import numpy
from astropy.io import fits
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pylab

# leftovers from super quick FITS to CSV file program
# # ask for an input file 
# filename = raw_input('Enter a FITS file to CSV-ize: ')

# # ask for an output file name
# output = raw_input('What would you like to call your new file?: ')

# Open the given fits file
hdulist = fits.open('WASP-43140308054812.FITS')
scidata = hdulist[0].data

## this is just for testing to make sure there are
## the numbers I think there are
count_lines = 0
count_elements = 0

for line in scidata:
    print line
    count_lines += 1

for element in scidata[0]:
    count_elements += 1

print "There are", count_lines, 'lines'
print "There are", count_elements, 'elements'

x_coordinates = []
y_coordinates = []
z_coordinates = []

# an attempt using range? Why not. 
# DO NOT like this dunno why
for line in range(0, count_lines):
    for element in range(0, count_elements):
        x_coordinates.append(element)
        y_coordinates.append(line)
        z_coordinates.append(scidata[line][element])


# create the graph!
graph = pylab.figure()
axes = Axes3D(graph)

axes.scatter(x_coordinates, y_coordinates, z_coordinates)

plt.show()

