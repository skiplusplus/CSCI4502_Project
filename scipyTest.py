#!/usr/bin/env python
import numpy
import math
from scipy.optimize import curve_fit
from matplotlib import pyplot
from os import system

h = 6.626 * 10**-34 		# Planck constant in J*s
#h = 4.136 * 10**-15 		# Planck constant in eV*s
#h = 6.625 * 10**-27 		# Planck constant in ergs*s
k = 1.38 * 10**-23  		# Boltzmann constant in J/K
#k = 8.617 * 10**-5		# Boltzmann constant in eV/K
#k = 1.38 * 10**-16		# Boltzmann constant in ergs/K
e = 2.71828 			# base of the natural logarithm
c = 299792458 			# speed of light in a vacuum in m/s

# blackbody radiation equation using wavelength & temp
def radiance_wavelength(wavelength, temp):
        return (2*h*(c**2)) / ((wavelength**5) * ((e**((h*c)/(wavelength*k*temp))) - 1))

# blackbody radiation equation using frequency & temp
def radiance_frequency(frequency, temp):
	return (2*h*(frequency**3)) / ((c**2) * ((e**((h*frequency)/(k*temp))) - 1))

# some test data, x values are wavelengths, y values aren't used yet
dataPoints = numpy.array([(0.000070, 0), (0.000160, 0), (0.000250, 0), (0.000350, 0), (0.000500, 0)])

# clear the terminal to make it easier to view results
system("clear")

# get wavelength data from dataPoints array
wavelengthData = dataPoints[:,0]
print "wavelengthData =", wavelengthData

# plug wavelength data into radiance equation
radianceData_wave = radiance_wavelength(wavelengthData, 18)
print "\nradianceData_wave =", radianceData_wave

# convert wavelength data to frequency data 
frequencyData = c / wavelengthData
print "\n\nfrequencyData =", frequencyData

# plug frequency data into radiance equation
radianceData_freq = radiance_frequency(frequencyData, 18)
print "\nradianceData_freq =", radianceData_freq, "\n"



#==================================================================
# Testing of the curve_fit function using a simple function
"""
points = numpy.array([(0, 0), (2, 9), (3, 29), (4, 65), (5, 125)])
# get x and y vectors
xData = points[:,0]
yData = points[:,1]

def func(x, a):
	return x**a

popt, pcov = curve_fit(func, xData, yData)

print "popt =", popt
print "xData =", xData

x_new = numpy.linspace(wavelengthData[0], xData[-1], 50)
y_new = func(x_new, popt[0])

pyplot.plot(xData, yData, 'ro', x_new, y_new)
pyplot.xlim([xData[0]-1, xData[-1] + 1 ])
pyplot.show()
"""
#==================================================================
#==================================================================


