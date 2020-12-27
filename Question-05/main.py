from astropy.constants import *
import astropy.units as u
from math import sqrt

time_correction_on_earth = 1 / ( 1 - (2 * G * M_earth / (c*c*R_earth)) )**0.5

for _ in range(int(input())):
    distance = float(input())
    distance = u.Quantity(distance, unit=u.m)

    v_square = (G * M_earth) / distance
    time_correction_on_satellite = 1 / ( 1 - (2 * G * M_earth / (c*c*distance)) )**0.5
    relativity_factor = 1 / (1 - (v_square / (c**2)))**0.5

    print("{:.5e}".format(((time_correction_on_satellite - time_correction_on_earth) + (relativity_factor - 1)) * 86400))