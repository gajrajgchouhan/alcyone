from astropy.constants import *
import astropy.units as u
from math import sqrt

time_correction_on_earth = 1 / ( 1 - (2 * G * M_earth / (c*c*R_earth)) )**0.5
time_correction_on_sun = 1 / ( 1 - (2 * G * M_sun / (c*c*R_sun)) )**0.5

for _ in range(int(input())):
    earth_sat, kuiper_sat = map(lambda x : u.Quantity(float(x), unit=u.m), input().split())

    v_square_earth_sat = (G * M_earth) / earth_sat
    v_square_sun_sat = (G * M_sun) / kuiper_sat

    time_correction_on_earth_sat = 1 / ( 1 - (2 * G * M_earth / (c*c*earth_sat)) )**0.5
    time_correction_on_kuiper_sat = 1 / ( 1 - (2 * G * M_sun / (c*c*kuiper_sat)) )**0.5
    
    relativity_factor_earth = 1 / (1 - (v_square_earth_sat / (c**2)))**0.5
    relativity_factor_kuiper = 1 / (1 - (v_square_sun_sat / (c**2)))**0.5

    print("{:.5e}".format(
            ((
                (time_correction_on_earth_sat - time_correction_on_earth) + (relativity_factor_earth - 1)
            ) + (
                (time_correction_on_kuiper_sat - time_correction_on_sun) + (relativity_factor_kuiper - 1)
            ))* 86400))