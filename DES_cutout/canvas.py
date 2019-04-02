from astropy.io import fits
import astropy.wcs as wcs
import numpy as np
import numpy

def canvas(hdulist, w, xc, yc, xw, yw):
    
    '''
        Description of the inputs:
        - hdulist: input image table
        - xc, yc: RA and DEC, respectively, of the object you want to cut from the input image
        - xw,yw: x and y width of the image you want to cut (in px)
        '''
    
    head = hdulist[0].header.copy()
    xx,yy = w.wcs_world2pix(xc,yc,1)
    
    #xmin,xmax = numpy.max([0,xx-xw]),numpy.min([head['NAXIS1'],xx+xw])
    #ymin,ymax = numpy.max([0,yy-yw]),numpy.min([head['NAXIS2'],yy+yw])
    
    xmin,xmax = np.int(numpy.max([0,xx-xw])),np.int(numpy.min([head['NAXIS1'],xx+xw]))
    ymin,ymax = np.int(numpy.max([0,yy-yw])),np.int(numpy.min([head['NAXIS2'],yy+yw]))
    
    # CRPIX = 2 element vector giving X and Y coordinates of reference pixel (def = NAXIS/2) in FITS convention (first pixel is 1,1)
    head['CRPIX1']-=xmin
    head['CRPIX2']-=ymin
    head['NAXIS1']=xmax-xmin
    head['NAXIS2']=ymax-ymin
    
    img = hdulist[0].data[ymin:ymax,xmin:xmax]
    return (img,head)

