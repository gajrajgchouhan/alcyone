from astropy.constants import *
import astropy.units as u
from math import sqrt

for _ in range(int(input())):
    distance = float(input())
    distance = u.Quantity(distance, unit=u.m)
    v_square = (G * M_earth) / distance
    time = 1 / (1 - (v_square / (c**2)))**0.5
    
    print(f"{time:.5E}")
    
