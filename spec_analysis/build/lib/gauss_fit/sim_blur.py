import numpy as np

def sim_blur(center, fit):
    '''
    sim_blur(center, sigma) blurs the cosima simulation to correspond with
    experimental data.
    center: energies generated from cosima_output
    fit: generated from fit_nrg_resolution
    '''
    return np.random.normal(center, fit[0]*(center)**2 + fit[1]*(center) + fit[2])
