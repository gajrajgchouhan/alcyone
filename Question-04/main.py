import os
from requests import get
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

# os.mkdir('./fits/')
# os.mkdir('./CoolSTAC')

for i in range(1, 111):
    url = f"http://archive.eso.org/dss/dss/image?ra=&dec=&equinox=J2000&name=M{i}&x=7&y=7&Sky-Survey=DSS1&mime-type=download-fits&statsmode=WEBFORM"
    image = get(url).content    
    image_file = f'./fits/M{i}.fits'
    with open(image_file, 'wb') as h:
        h.write(image)
    print('downloaded fits of M', i)
    image_data = fits.getdata(image_file, ext=0)
    plt.figure()
    plt.imshow(image_data, cmap='gray')
    plt.colorbar()
    plt.title(f'M{i}')
    plt.savefig(f'./CoolSTAC/M{i}.png')
    plt.close()