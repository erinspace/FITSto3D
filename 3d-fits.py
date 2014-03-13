## generate a 3D plot from a table of FITS values

import numpy
from astropy.io import fits

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
    count_lines += 1

for element in scidata[1]:
    count_elements += 1

print "There are", count_lines, 'lines'
print "There are", count_elements, 'elements'

# scidata = list(scidata)

threeD_array = []

# # attempt using numpy iteration - dosent work
# # get error: IndexError: index 1271 is out of bounds for size 650
# for line in numpy.nditer(scidata):
#     inner_array = []
#     for element in numpy.nditer(scidata[line]):
#         inner_array.append(element)
#         inner_array.append(line)
#         inner_array.append(scidata[line][element])
#         threeD_array.append(inner_array)
#         inner_array = []

# # attempt using "normal" loops... same error!
# for line in scidata:
#     inner_array = []
#     for element in scidata[line]:
#         inner_array.append(element)
#         inner_array.append(line)
#         inner_array.append(scidata[line][element])
#         threeD_array.append(inner_array)
#         inner_array = []


# an attempt using range? Why not. 
# DO NOT like this cause it's hard coded! But it works? 
for line in range(0, 500):
    inner_array = []
    for element in range(0, scidata[0].size):
        inner_array.append(element)
        inner_array.append(line)
        inner_array.append(scidata[line][element])
        threeD_array.append(inner_array)
        inner_array = []

