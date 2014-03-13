## generate a 3D plot from a table of FITS values

import numpy
from astropy.io import fits

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
    count_lines += 1

for element in scidata[1]:
    count_elements += 1

print "There are", count_lines, 'lines'
print "There are", count_elements, 'elements'


threeD_array = []

for line in scidata:
    inner_array = []
    for element in scidata[line]:
        inner_array.append(element)
        inner_array.append(line)
        inner_array.append(scidata[line][element])
        threeD_array.append(inner_array)
