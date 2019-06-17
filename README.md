# Cosmo
canvas.py (Cut ANd VAlidate Stamps) is a function which extracts postage stamps from COADD DES images. The code example.py shows how to call this function and produce stamps. 
The algorithm is part of the pipeline written to produce the DES Y1 Morphology Catalogue (Tarsitano et al., 2018). For more details see the publication http://adsabs.harvard.edu/doi/10.1093/mnras/sty1970 .
If you use this code as a cutout service for your project, please cite the paper above in your publication.

## How to use CANVAS
In the DES_cutouts directory the script example.py shows how to use canvas:
* It takes the name od the coadd image ("coaddname") and the output directory as arguments. The latter will be used to store the cutout stamps.;
* then it reads the catalogue associated to the image. In this example it is assumed that the catalogue is names as "coadname_cat.fits";
* it selects the stamps to cut, according to the following selection function: ('CLASS_STAR'<0.9 & 'FLAGS'==0 & 'MAG_AUTO'<99. & 'FLUX_RADIUS'>0. & 'KRON_RADIUS'>0);
* it calls the canvas function, which needs the coordinate of the galaxy at the centre of the stamp and the size. The half-width of the stamp is set to 3 times the Kron radius of the galaxy, inteded as the product between teh SExtractor KRON_RADIUS and A_IMAGE of the galaxy itself. The cutout stamps are saved in the output directory given as an argument.
