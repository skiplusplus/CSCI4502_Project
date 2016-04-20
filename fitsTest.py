
import numpy 
from scipy.optimize import curve_fit
from astropy.io import fits
#hdulist = fits.open('practiceData/HIGAL0154n015_250_RM.fits')
hdulist = fits.open('70aca.fits')

info = hdulist.info()
print info
print hdulist[0].header[:5]
data = hdulist[0].data
print data[201, 273]
print data[501, 573]
print data[1501, 1512]
print data[1901, 1911]

hdulist.close()

