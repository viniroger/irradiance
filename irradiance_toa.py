# Parameters to calculate irradiance at TOA
doy = 214
hour = 12
minute = 0
lat = -15.60083333
lon = -47.71305556

def d_cosz(doy, hour, minutehour, lat, lon):
	"""
	Calculate earth-sun distance and cosine of the zenith angle
	"""
	from math import pi
	import numpy as np
	minute = 60*hour + minutehour
	
	# Day angle (in radians)
	day_angle = ((360.*(doy-1))/365.15)*pi/180.
	# Solar declination (in radians)
	dec = (0.006918 - 0.399912 * np.cos(day_angle) + 0.070257 * np.sin(day_angle) - 0.006758 * np.cos(2 * day_angle) + 0.000907 * np.sin(2 * day_angle) - 0.002697 * np.cos(3 * day_angle) + 0.001480 * np.sin(3 * day_angle))
	
	# Earth-Sun distance from day of year
	d_astro = 1.00011 + 0.034221 * np.cos(day_angle) + 0.00128 * np.sin(day_angle) + 0.000719 * np.cos(2 * day_angle) + 0.000077 * np.sin(2 * day_angle)
	
	# Time Equation (in minutes)
	eqtime = (0.000075 + 0.001868 * np.cos(day_angle) - 0.032077 * np.sin(day_angle) - 0.014615 * np.cos(2 * day_angle) - 0.040849 * np.sin(2 * day_angle)) * ((180 * 4)/(pi))
	# Total time translated (solar time, in hours)
	tcorr = (minute/60. + lon/15. + eqtime/60.)
	# Hour angle (in radians)
	H0 = ((12. - tcorr) * 15.) * pi/180.
	
	# Zenital angle cosine
	cosZ = (np.sin(dec) * np.sin(lat*pi/180.)) + (np.cos(dec) * np.cos(lat*pi/180.) * np.cos(H0))
	# Zenital angle (in degrees)
	Z = np.arccos(cosZ)*180./pi
	
	return(d_astro, cosZ, Z)

# Calculate TOA elements
d_astro, cosZ, Z = d_cosz(doy, hour, minute, lat, lon)
# Calculate Top Of Atmosphere Irradiance (TOA)
toa = 1367 * d_astro * cosZ

print(d_astro, cosZ, Z)
print(toa)
