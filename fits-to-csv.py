# Python program to convert a FITS file
# to a CSV you can open in Excel
# written by Erin for Jim! 

import numpy
from astropy.io import fits

# ask for an input file 
filename = raw_input('Enter a FITS file to CSV-ize: ')

# ask for an output file name
output = raw_input('What would you like to call your new file?: ')

# Open the given fits file
hdulist = fits.open(filename)
scidata = hdulist[0].data

# save your new file as a csv
numpy.savetxt(output, scidata, fmt='%d', delimiter=',')
