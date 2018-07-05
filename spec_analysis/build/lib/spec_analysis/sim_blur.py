import numpy as np

def sim_blur(center, fit):
    '''
    cnts, bin_centers = sim_blur(center, sigma) blurs the cosima simulation to correspond with
    experimental data.
    center: energies generated from cosima_output
    fit: generated from fit_nrg_resolution
    '''

    nrgsb_fast = np.random.normal(center, fit[0]*(center)**2 + fit[1]*(center) + fit[2])
    cnts, bin_edges = np.histogram(nrgsb_fast, bins=np.arange(0, 3001, 3))
    bin_centers = bin_edges[:-1] + np.diff(bin_edges) / 2.
    return cnts, bin_centers
