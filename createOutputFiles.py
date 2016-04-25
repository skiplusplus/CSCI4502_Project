#!/usr/bin/env python

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# File:  createOutputFiles.py
# Author:  Jacob C. Levine
# Class Project:  CSCI 4502 Data Mining
# Date created:  4/24/16
# Description: 
#        Creates a fits file called maxIntensities.fits
#        filled with NaNs located in the 
#        /home/user/DataMining/Results/ directory. 
# Arguments: 
#        wavelength: either 70, 160, 250, 350, or 500
# Usage:
#        createOutputFiles.py wavelength
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import sys
import numpy
from astropy.io import fits

wavelength = sys.argv[1]
print "Creating output file for", wavelength, "um wavelength"
shape = (6000, 40501)
#shape = (40501, 6000)
fill_value = numpy.nan
dtype = numpy.float32
order = 'C'

newDataArray = numpy.full(shape, fill_value, dtype, order)
new_hdu = fits.PrimaryHDU(data=newDataArray)

newFilename = "fits/" + wavelength + "maxIntensities.fits"
new_hdu.writeto(newFilename, clobber=True)
new_hdulist = fits.open(newFilename)
new_data = new_hdulist[0].data
new_hdulist.close()

