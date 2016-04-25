#!/usr/bin/env python

#++++++++++++++++++++++++++++++++++++++++++++++
# File:  getMaxIntensities.py
# Author:  Jacob C. Levine
# Class Project:  CSCI 4502 Data Mining
# Date created:  4/23/16
#++++++++++++++++++++++++++++++++++++++++++++++

import multiprocessing
import sys
import numpy
#from scipy.optimize import curve_fit
from astropy.io import fits


#wavelengths = ["70", "160", "250", "350", "500"]
#sourceDataDimensions = (40501, 6000)
sourceDataDimensions = (6000, 40501) 

directory = "fits/"

#open files for reading
r70_hdulist = fits.open(directory + "70buc.fits")
r70_data = r70_hdulist[0].data
r70_hdulist.close()

r160_hdulist = fits.open(directory + "160buc.fits")
r160_data = r160_hdulist[0].data
r160_hdulist.close()

r250_hdulist = fits.open(directory + "250buc.fits")
r250_data = r250_hdulist[0].data
r250_hdulist.close()

r350_hdulist = fits.open(directory + "350buc.fits")
r350_data = r350_hdulist[0].data
r350_hdulist.close()

r500_hdulist = fits.open(directory + "500buc.fits")
r500_data = r500_hdulist[0].data
r500_hdulist.close()

datalist = ["r70_data", "r160_data", "r250_data", "r350_data", "r500_data"]

#open files for writing
w70_hdulist = fits.open(directory + "70maxIntensities.fits")
w70 = w70_hdulist[0].data
#w70_hdulist.close()

w160_hdulist = fits.open(directory + "160maxIntensities.fits")
w160 = w160_hdulist[0].data
#w160_hdulist.close()

w250_hdulist = fits.open(directory + "250maxIntensities.fits")
w250 = w250_hdulist[0].data
#w250_hdulist.close()

w350_hdulist = fits.open(directory + "350maxIntensities.fits")
w350 = w350_hdulist[0].data
#w350_hdulist.close()

w500_hdulist = fits.open(directory + "500maxIntensities.fits")
w500 = w500_hdulist[0].data
#w500_hdulist.close()




writelist = [w70, w160, w250, w350, w500]

'''

# Function for iterating through each coordinate
def getMaxVals(xMin, xMax, yMin, yMax):
	wavelengths = ["70", "160", "250", "350", "500"]
	for x in range(xMin, xMax):
		for y in range(yMin, yMax):
				
		        maxIntensity = 0.0
		
			# Check each wavelength to see which is max
		        for wavelength in wavelengths:
               	                currentIntensity = source_data[x, y]
		                if currentIntensity > maxIntensity:
		                        maxIntensity = currentIntensity
		                        wavelengthWithMaxVal = wavelength
		
		                source_hdulist.close()
		
			# Write max intensity to corresponding output file
		        if maxIntensity != 0.0:
		                destinationFilename = "/home/user/DataMining/Results/" + wavelength + "maxIntensities.fits"
		                destination_hdulist = fits.open(destinationFilename)
		                destination_data = destination_hdulist[0].data
				destination_data[x, y] = 500
		                destination_hdulist.writeto(destinationFilename, clobber=True)
		                destination_hdulist.close()
		
	return

numProcesses = 40
for i in range(0, numProcesses):
	xMin = i*4050//numProcesses
	xMax = (i+1)*4050//numProcesses
	yMin = i*600//numProcesses
	yMax = (i+1)*600//numProcesses
	p = multiprocessing.Process(target=getMaxVals, args=(xMin,xMax,yMin,yMax))
	p.start()
	p.join()

'''
'''
p1 = multiprocessing.Process(target=getMaxVals, args=(  0,  40,  0,  6) )
p2 = multiprocessing.Process(target=getMaxVals, args=( 41,  81,  7, 12) )
p3 = multiprocessing.Process(target=getMaxVals, args=( 82, 122, 13, 18) )
p4 = multiprocessing.Process(target=getMaxVals, args=(123, 163, 19, 24) )
p5 = multiprocessing.Process(target=getMaxVals, args=(164, 204, 25, 30) )
p6 = multiprocessing.Process(target=getMaxVals, args=(205, 245, 31, 36) )
p7 = multiprocessing.Process(target=getMaxVals, args=(246, 286, 37, 42) )
p8 = multiprocessing.Process(target=getMaxVals, args=(287, 327, 43, 48) )
p9 = multiprocessing.Process(target=getMaxVals, args=(328, 368, 49, 54) )
p0 = multiprocessing.Process(target=getMaxVals, args=(369, 405, 55, 60) )

p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()
p7.start()
p8.start()
p9.start()
p0.start()

p1.join()
p2.join()
p3.join()
p4.join()
p5.join()
p6.join()
p7.join()
p8.join()
p9.join()
p0.join()
'''



'''
for wavelength in wavelengths: 
	filename = "/home/user/DataMining/DMsections/" + wavelength + "buc.fits"

	source_hdulist = fits.open(filename)
	source_info = source_hdulist.info()
	print source_info
	source_hdulist.close()
'''



# Iterate through each coordinate
for x,y in numpy.ndindex(sourceDataDimensions):

	'''	
	# progress indicator
	x_milestone = 1
	y_milestone = 1
	percent = 1
	
	if x == x_milestone:
	#if x == x_milestone and y == y_milestone:
		print str(percent) + "% complete..."
		x_milestone += 60
		#y_milestone += .06
		#x_milestone += 405
		#y_milestone += 60
		percent += 1
	'''

	#print "x =", x, "y =", y
        maxIntensity = 0.0

	# Check each wavelength to see which is max
        for wavelength in datalist:
                #sourceFilename = "/home/user/DataMining/DMsections/" + wavelength + "buc.fits"

		#if we want to open and close on the fly
		#sourceFilename = "/home/jon/Dropbox/CSCI/4502/project/code/fits/" + wavelength + "buc.fits"

		#source_hdulist = fits.open(sourceFilename)
                #source_data = source_hdulist[0].data

                currentIntensity = eval(wavelength)[x, y]
		#if currentIntensity == numpy.nan:
		#print currentIntensity
                if currentIntensity > maxIntensity:
                        maxIntensity = currentIntensity
			#print "maxIntensity set to", maxIntensity
                        wavelengthWithMaxVal = wavelength

                #source_hdulist.close()



	# Write max intensity to corresponding output data variables
	if maxIntensity != 0.0:
		#print "found a max ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^" + wavelengthWithMaxVal
		if wavelengthWithMaxVal == "r70_data":
			w70[x, y] = 500
			#print "max is 70 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
		elif wavelengthWithMaxVal == "r160_data":
			w160[x, y] = 500
			#print "max is 160 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
		elif wavelengthWithMaxVal == "r250_data":
			w250[x, y] = 500
			#print "max is 250 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
		elif wavelengthWithMaxVal == "r350_data":
			w350[x, y] = 500
			#print "max is 350 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
		elif wavelengthWithMaxVal == "r500_data":
			w500[x, y] = 500
			#print "max is 500 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

# Write max intensity to corresponding output data files

w70_hdulist.writeto(directory + "70maxIntensities.fits", clobber=True)
w160_hdulist.writeto(directory + "160maxIntensities.fits", clobber=True)
w250_hdulist.writeto(directory + "250maxIntensities.fits", clobber=True)
w350_hdulist.writeto(directory + "350maxIntensities.fits", clobber=True)
w500_hdulist.writeto(directory + "500maxIntensities.fits", clobber=True)

# Close files
w70_hdulist.close()
w160_hdulist.close()
w250_hdulist.close()
w350_hdulist.close()
w500_hdulist.close()

'''
        if maxIntensity != 0.0:
                destinationFilename = "/home/jon/Dropbox/CSCI/4502/project/code/fits/" + wavelength + "maxIntensities.fits"
                destination_hdulist = fits.open(destinationFilename)
                destination_data = destination_hdulist[0].data
                print "writing to", destinationFilename
		destination_data[y, x] = 500
                #destination_hdulist.writeto(destinationFilename, clobber=True)
                destination_hdulist.close()
'''






