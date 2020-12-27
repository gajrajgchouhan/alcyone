import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
from pytz import timezone as pytimezone
from matplotlib.collections import LineCollection

from astropy import coordinates
from astropy import units as u
from astropy.coordinates import SkyCoord

from skyfield import api, units
from skyfield.api import Star, load
from skyfield.data import hipparcos, mpc, stellarium
from skyfield.projections import build_stereographic_projection
from skyfield.constants import GM_SUN_Pitjeva_2005_km3_s2 as GM_SUN

ts = api.load.timescale()

Year, Month, Date, Hour, Minutes, Longitude, Latitude, Azimuth, Altitude = map(float, input().split())

t = ts.from_datetime(datetime(int(Year), int(Month), int(Date), int(Hour), int(Minutes), tzinfo=pytimezone('Asia/Kolkata')))

topos = api.Topos(latitude_degrees=Latitude, longitude_degrees=Longitude)
observer = topos.at(t)
pos = observer.from_altaz(alt_degrees=Altitude, az_degrees=Azimuth)
ra, dec, distance = pos.radec()

# Part A
print('Right ascension', ra)
print('Declination', dec)

print('Constellation', coordinates.get_constellation(SkyCoord(ra.hours*u.hour, dec.degrees*u.degree)))

def plot_constellation(hours, degrees, t, name):

    planets = load('de421.bsp')
    earth = planets['earth']

    o = Star(ra_hours=hours,
                   dec_degrees=degrees)

    astrometric = earth.at(t).observe(o)

    # An ephemeris from the JPL provides Sun and Earth positions.

    eph = load('de421.bsp')
    sun = eph['sun']
    earth = eph['earth']

    # The Hipparcos mission provides our star catalog.

    with load.open(hipparcos.URL) as f:
        stars = hipparcos.load_dataframe(f)

    # And the constellation outlines come from Stellarium.  We make a list
    # of the stars at which each edge stars, and the star at which each edge
    # ends.

    url = ('https://raw.githubusercontent.com/Stellarium/stellarium/master'
           '/skycultures/western_SnT/constellationship.fab')

    with load.open(url) as f:
        constellations = stellarium.parse_constellations(f)

    edges = [edge for name, edges in constellations for edge in edges]
    edges_star1 = [star1 for star1, star2 in edges]
    edges_star2 = [star2 for star1, star2 in edges]

    projection = build_stereographic_projection(astrometric)
    field_of_view_degrees = 70.0
    limiting_magnitude = 5.0

    # Now that we have constructed our projection, compute the x and y
    # coordinates that each star and the comet will have on the plot.

    star_positions = earth.at(t).observe(Star.from_dataframe(stars))
    stars['x'], stars['y'] = projection(star_positions)

    # Create a True/False mask marking the stars bright enough to be
    # included in our plot.  And go ahead and compute how large their
    # markers will be on the plot.

    bright_stars = (stars.magnitude <= limiting_magnitude)
    magnitude = stars['magnitude'][bright_stars]
    marker_size = (0.5 + limiting_magnitude - magnitude) ** 2.0

    # The constellation lines will each begin at the x,y of one star and end
    # at the x,y of another.  We have to "rollaxis" the resulting coordinate
    # array into the shape that matplotlib expects.

    xy1 = stars[['x', 'y']].loc[edges_star1].values
    xy2 = stars[['x', 'y']].loc[edges_star2].values
    lines_xy = np.rollaxis(np.array([xy1, xy2]), 1)

    # Time to build the figure!

    fig, ax = plt.subplots(figsize=[9, 9])

    # Draw the constellation lines.

    ax.add_collection(LineCollection(lines_xy, colors='#00f2'))

    # Draw the stars.

    ax.scatter(stars['x'][bright_stars], stars['y'][bright_stars],
               s=marker_size, color='k')

    # Finally, title the plot and set some final parameters.

    angle = np.pi - field_of_view_degrees / 360.0 * np.pi
    limit = np.sin(angle) / (1.0 - np.cos(angle))

    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    # ax.xaxis.set_visible(False)
    # ax.yaxis.set_visible(False)
    ax.set_aspect(1.0)

    # Save.

    fig.savefig(name, bbox_inches='tight')
   
    return

plot_constellation(ra.hours, dec.degrees, t, 'PartA')

t = ts.from_datetime(datetime(int(Year), int(Month), int(Date), 10, 0, tzinfo=pytimezone('Asia/Kolkata')))
topos = api.Topos(latitude_degrees=Latitude, longitude_degrees=Longitude)
observer = topos.at(t)

pos = observer.from_altaz(alt_degrees=90, az_degrees=0)
ra, dec, distance = pos.radec()
plot_constellation(ra.hours, dec.degrees, t, 'JustAbove.png')
print('Constellation', coordinates.get_constellation(SkyCoord(ra.hours*u.hour, dec.degrees*u.degree)))

pos = observer.from_altaz(alt_degrees=270, az_degrees=0)
ra, dec, distance = pos.radec()
plot_constellation(ra.hours, dec.degrees, t, 'JustBelow.png')
print('Constellation', coordinates.get_constellation(SkyCoord(ra.hours*u.hour, dec.degrees*u.degree)))

directions = {"N":0, "E":90, "S":180, "W":270, "NE":45, "NW":315, "SE":135, "SW":225}
for d in directions:
    pos = observer.from_altaz(alt_degrees=directions[d], az_degrees=0)
    ra, dec, distance = pos.radec()
    plot_constellation(ra.hours, dec.degrees, t, d+'.png')
    print('Direction', d, 'Constellation', coordinates.get_constellation(SkyCoord(ra.hours*u.hour, dec.degrees*u.degree)))
