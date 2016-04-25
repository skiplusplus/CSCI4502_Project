#!/usr/bin/env python

import numpy 
#from scipy.optimize import curve_fit
from astropy.io import fits

'''
info = hdulist.info()
print hdulist[0].header[:5]
data = hdulist[0].data
hdulist.close()
'''

wavelengths = [70, 160, 250, 350, 500]

# Create source data fits files
for wavelength in wavelengths:
	sourceDataArray = numpy.random.random((3,4)).astype(numpy.float32)
	sourceDataArray *= 1000
	source_hdu = fits.PrimaryHDU(data=sourceDataArray)

	sourceFilename = "practiceData/sourceFitsFile" + str(wavelength) + ".fits"
	source_hdu.writeto(sourceFilename, clobber=True)
	source_hdulist = fits.open(sourceFilename)

	#source_info = source_hdulist.info()
	#print source_info
	source_data = source_hdulist[0].data
	print sourceFilename + ":"
	print source_data

	source_hdulist.close()



# Create new, empty (nan's) fits files
for wavelength in wavelengths:
	shape = (3,4)
	fill_value = numpy.nan
	dtype = numpy.float32
	order = 'C'

	newDataArray = numpy.full(shape, fill_value, dtype, order)
	new_hdu = fits.PrimaryHDU(data=newDataArray)

	newFilename = "practiceData/newFitsFile" + str(wavelength) + ".fits"
	new_hdu.writeto(newFilename, clobber=True)
	new_hdulist = fits.open(newFilename)
	new_data = new_hdulist[0].data
	new_hdulist.close()



# Iterate through source files and insert max intensities into new files
for x,y in numpy.ndindex((3,4)):

	maxIntensity = 0.0

	for wavelength in wavelengths:
		sourceFilename = "practiceData/sourceFitsFile" + str(wavelength) + ".fits"
		source_hdulist = fits.open(sourceFilename)
        	source_data = source_hdulist[0].data
		currentIntensity = source_data[x, y]

		if currentIntensity > maxIntensity:
			maxIntensity = currentIntensity
			wavelengthWithMaxVal = wavelength

        	source_hdulist.close()

	if maxIntensity != 0.0:
		destinationFilename = "practiceData/newFitsFile" + str(wavelengthWithMaxVal) + ".fits"
		destination_hdulist = fits.open(destinationFilename)
		destination_data = destination_hdulist[0].data
		destination_data[x, y] = maxIntensity
		destination_hdulist.writeto(destinationFilename, clobber=True)
		destination_hdulist.close()



# print data in new fits files
for wavelength in wavelengths:
        newFilename = "practiceData/newFitsFile" + str(wavelength) + ".fits"
        new_hdulist = fits.open(newFilename)
        new_data = new_hdulist[0].data
        new_hdulist.close()

	print newFilename
	print new_data



