from astropy.constants import *
import astropy.units as u
from math import sqrt

def dilation(mass, distance):
    v_square = (G * mass) / distance
    time = 1 / (1 - (v_square / (c**2)))**0.5

    return time

for _ in range(int(input())):
    ark, messiah = map(float, input().split())
    ark = u.Quantity(ark, unit=u.m)
    messiah = u.Quantity(messiah, unit=u.m)
    dilation(M_earth, ark)
    dilation(M_sun, messiah)
    
    
    print(f"{time:.5E}")
    
