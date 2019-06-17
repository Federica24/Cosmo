import numpy as np
from astropy.io import fits
import astropy.wcs as wcs
import argparse
from canvas import canvas
import time

t_begin = time.time()

# Read the arguments
parser = argparse.ArgumentParser()
parser.add_argument("coaddname", type=str,
                    help="tilenumber to access the data")
parser.add_argument("outputdir", type=str,
                    help="storage folder for the stamps")
args = parser.parse_args()

# Read the catalogue
coadd_tile = args.coaddname
pha_list = fits.open(coadd_tile + '_cat.fits')
pha_data = pha_list[1].data

# Open the fits image
hdulist_tile = fits.open(coadd_tile + '.fits')
w_tile = wcs.WCS(hdulist_tile[0].header)

# Select the objects of interest
number = pha_data['NUMBER']
mask = (pha_data['CLASS_STAR']<0.9) & (pha_data['FLAGS']==0) & (pha_data['MAG_AUTO']<99.)& (pha_data['FLUX_RADIUS']>0.) & (pha_data['KRON_RADIUS']>0.)
selection = number[mask]
print 'Number of postage stamps to create =', len(selection)

# Set the output directory
output_dir = args.outputdir
if output_dir[-1] != "/":
    output_dir = output_dir+"/"

# Cut the stamps
for n in selection:
    
    obj = n-1
    ra = pha_data['ALPHAWIN_J2000'][obj]
    dec = pha_data['DELTAWIN_J2000'][obj]
    a_image = pha_data['A_IMAGE'][obj]
    kr = float(pha_data['KRON_RADIUS'][obj])

    input_size = round(kr*a_image,0)*6
    if input_size % 2 == 0:
        input_size = (input_size-1)
    wd = input_size*1./2

    nameout = coadd_tile + '_' + str(n) + '.fits'
    img = canvas(hdulist_tile,w_tile,ra,dec,wd,wd)
    newfile = fits.PrimaryHDU(data=img[0],header=img[1])
    newfile.writeto(output_dir + nameout,clobber=True,checksum=True)

t_end = time.time()
print("Time Elapsed for the search: %6.4f" % (t_end-t_begin))
