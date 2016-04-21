#!/usr/bin/env python
import numpy
import math
from scipy.optimize import curve_fit
from matplotlib import pyplot


h = 6.626 * 10**-34             # Planck constant in J*s
k = 1.38 * 10**-23              # Boltzmann constant in J/K
e = 2.71828                     # base of the natural logarithm
c = 299792458                   # speed of light in a vacuum in m/s


# blackbody radiation equation using frequency & temp
def radiance_frequency(frequency, temp):
        return (2*h*(frequency**3)) / ((c**2) * ((e**((h*frequency)/(k*temp))) - 1))

# some test data, x values are wavelengths, y values aren't used yet
dataPoints = numpy.array([(0.000070, 0), (0.000160, 0), (0.000250, 0), (0.000350, 0), (0.000500, 0)])

# get wavelength data from dataPoints array
wavelengthData = dataPoints[:,0]
print "wavelengthData =", wavelengthData, "\n"

# convert wavelength data to frequency data 
frequencyData = c / wavelengthData

# plug frequency data into radiance equation
radianceData_freq = radiance_frequency(frequencyData, 18)

# convert radiance values to MJy/sr
intensityData = radianceData_freq / 10**-20
print "\nintensityData =", intensityData, "\n"

# 
popt, pcov = curve_fit(radiance_frequency, wavelengthData, intensityData)
print "popt =", popt

