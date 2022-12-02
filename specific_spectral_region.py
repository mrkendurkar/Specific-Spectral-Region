from specutils import Spectrum1D, analysis, manipulation, SpectralRegion, fitting
from astropy.io import fits
import matplotlib.pyplot as plt
import astropy.units as u
import astropy.wcs as wcs
from astropy.nddata import StdDevUncertainty
import numpy as np
from specutils.fitting import fit_generic_continuum
from astropy.modeling import models
from astropy import units as u
from specutils.spectra import Spectrum1D, SpectralRegion
from specutils.fitting import fit_generic_continuum

spec1 = Spectrum1D.read("1.fits", format='wcs1d-fits')
spec2 = Spectrum1D.read("2.fits", format='wcs1d-fits')
spec3 = Spectrum1D.read("3.fits", format='wcs1d-fits')
spec4 = Spectrum1D.read("4.fits", format='wcs1d-fits')
spec5 = Spectrum1D.read("5.fits", format='wcs1d-fits')
spec6 = Spectrum1D.read("6.fits", format='wcs1d-fits')
spec7 = Spectrum1D.read("7.fits", format='wcs1d-fits')
spec8 = Spectrum1D.read("8.fits", format='wcs1d-fits')
spec9 = Spectrum1D.read("9.fits", format='wcs1d-fits')
spec10 = Spectrum1D.read("10.fits", format='wcs1d-fits')


spec1_slice = spec1[0]
spec1 = Spectrum1D(spectral_axis=spec1.wavelength, flux = spec1.flux)
spec1_slice = spec1[4800*u.angstrom:4900*u.angstrom]



spec2_slice = spec2[0]
spec2 = Spectrum1D(spectral_axis=spec2.wavelength, flux = spec2.flux)
spec2_slice = spec2[4800*u.angstrom:4900*u.angstrom]


spec3_slice = spec3[0]
spec3 = Spectrum1D(spectral_axis=spec1.wavelength, flux = spec3.flux)
spec3_slice = spec3[4800*u.angstrom:4900*u.angstrom]


spec4_slice = spec4[0]
spec4 = Spectrum1D(spectral_axis=spec4.wavelength, flux = spec4.flux)
spec4_slice = spec4[4800*u.angstrom:4900*u.angstrom]

spec5_slice = spec5[0]
spec5 = Spectrum1D(spectral_axis=spec5.wavelength, flux = spec5.flux)
spec5_slice = spec5[4800*u.angstrom:4900*u.angstrom]


spec6_slice = spec6[0]
spec6 = Spectrum1D(spectral_axis=spec6.wavelength, flux = spec6.flux)
spec6_slice = spec6[4800*u.angstrom:4900*u.angstrom]


spec7_slice = spec7[0]
spec7 = Spectrum1D(spectral_axis=spec7.wavelength, flux = spec7.flux)
spec7_slice = spec7[4800*u.angstrom:4900*u.angstrom]


spec8_slice = spec8[0]
spec8 = Spectrum1D(spectral_axis=spec8.wavelength, flux = spec8.flux)
spec8_slice = spec8[4800*u.angstrom:4900*u.angstrom]


spec9_slice = spec9[0]
spec9 = Spectrum1D(spectral_axis=spec9.wavelength, flux = spec9.flux)
spec9_slice = spec9[4800*u.angstrom:4900*u.angstrom]


spec10_slice = spec10[0]
spec10 = Spectrum1D(spectral_axis=spec10.wavelength, flux = spec10.flux)
spec10_slice = spec10[4800*u.angstrom:4900*u.angstrom]



#increase the size of the legend to make it visible on the graph

fig, ax = plt.subplots(figsize=(35,85))


ax.plot(spec1_slice.wavelength, spec1_slice.flux[0],lw=2.5, ms=1.5, color = 'tab:blue')

ax.scatter(spec2_slice.wavelength, spec2_slice.flux[0]+50,  lw=0.5, color = 'tab:orange')

ax.plot(spec3_slice.wavelength, spec3_slice.flux[0]+100, lw=2.5, ms=0.5, color = 'tab:green')

ax.scatter(spec4_slice.wavelength, spec4_slice.flux[0]+150, lw=0.5, color = 'tab:red')

ax.plot(spec5_slice.wavelength, spec5_slice.flux[0]+200, lw=2.5, ms=0.5, color = 'tab:purple')

ax.scatter(spec6_slice.wavelength, spec6_slice.flux[0]+250, lw=0.5, color = 'tab:brown')

ax.plot(spec7_slice.wavelength, spec7_slice.flux[0]+300, lw=2.5, ms=0.5, color = 'tab:pink')

ax.scatter(spec8_slice.wavelength, spec8_slice.flux[0]+350, lw=0.5, color = 'tab:gray')

ax.plot(spec9_slice.wavelength, spec9_slice.flux[0]+400, lw=2.5, ms=0.5, color = 'tab:olive')

ax.scatter(spec8_slice.wavelength, spec8_slice.flux[0]+450, lw=0.5, color = 'tab:cyan')

ax.plot(spec9_slice.wavelength, spec9_slice.flux[0]+500, lw=2.5, ms=0.5, color = 'rosybrown')

ax.scatter(spec10_slice.wavelength, spec10_slice.flux[0]+550, lw=0.5, color = 'brown')


plt.legend(['1918-06-13, UT:07', '1918-06-26, UT:08', '1918-06-29, UT:07', '1918-06-29, UT:08', 
'1918-07-02, UT:08', '1918-07-05, UT:07', '1918-07-06, UT:08', '1918-07-06, UT:08', '1918-07-06, UT:09', 
'1918-07-11, UT:07', '1918-07-11, UT:07', '1918-07-15, UT:06', '1918-07-15, UT:06', '1918-07-16, UT:07', 
'1918-07-16, UT:07', '1918-07-21, UT:06'],
 loc="upper left", prop={'size': 25})

# to increase the font size on x and y axis
ax.tick_params(axis='both', which='major', labelsize=50)
ax.tick_params(axis='both', which='minor', labelsize=30)
ax.tick_params(axis='both', which='minor', labelsize=30)
ax.tick_params(axis='both', which='minor', labelsize=30)

#ax.set_title("V603_Aql", size = 65)
plt.locator_params(axis='x', nbins=10)
plt.locator_params(axis='y', nbins=10)

ax.set_xlabel("Wavelength (Angstrom)", size=50)
ax.set_ylabel("Relative intensity", size=50)

# for grid pattern (type True) if needed
ax.grid(False)
fig.patch.set_facecolor('xkcd:white')
