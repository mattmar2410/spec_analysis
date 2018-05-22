from becquerel import Spectrum
import numpy as np
import matplotlib.pyplot as plt
import os
from copy import deepcopy
from .gamma_energies import gamma_energies
from .calibration import spectrum_calibration
from lmfit.models import GaussianModel
from lmfit.models import LinearModel
import operator
import math

'''
spectrum_gauss_fit takes an input spectrum and finds the peaks of the
spectrum and fits a gaussian curve to the photopeaks
'''
def spectrum_gauss_fit(energy_data, cnts_data, energy_spectrum, channel_width):
    '''
    spectrum_gauss_fit takes an input spectrum and finds the peaks of the
    spectrum and fits a gaussian curve to the photopeaks and returns the
    amplitude and sigma of the gaussian peak.
    Make sure the spectrum is calibrated first.
    spectrum_gauss_fit(energy_data, cnts_data, energy_spectrum, channel_width)
    energy_data: .energies_kev that has been calibrated from becquerel
    cnts_data: .cps_vals from becquerel spectrum
    energy_spectrum: an array of gamma energies generated from gamma_energies
    channel_width: width of the peak for analysis purposes
    '''
    sigma_list = []; amplitude_list = []
    for erg in energy_spectrum:
        x_loc = list(filter(lambda x:(erg-3)<energy_data[x]<(erg+3),range(len(energy_data))))
        x_loc_pk = range(int(x_loc[0]-5), int(x_loc[0]+5))
        pk_cnt = np.argmax(cnts_data[x_loc_pk])
        ch_width = range(int(x_loc_pk[pk_cnt]-channel_width), int(x_loc_pk[pk_cnt]+channel_width))

        calibration = energy_data[ch_width]
        real_y_gauss = cnts_data[ch_width]
        x = np.asarray(calibration)
        real_y = np.asarray(real_y_gauss)

        mod_gauss  = GaussianModel(prefix='g1_')
        line_mod = LinearModel(prefix='line')
        pars = mod_gauss.guess(real_y, x=x)
        pars.update(line_mod.make_params(intercept=real_y.min(), slope=0))
        pars.update(mod_gauss.make_params())
        pars['g1_center'].set(x[np.argmax(real_y)], min=x[np.argmax(real_y)]\
        - 3)
        pars['g1_sigma'].set(3, min=0.25)
        pars['g1_amplitude'].set(max(real_y), min=max(real_y)-10)
        mod = mod_gauss + line_mod
        out  = mod.fit(real_y, pars, x=x)

        #print("The amplitude sum is %0.2f" % sum(real_y))
        gauss_x = []; gauss_y = []; parameter_list_1 = []
        real_y_gauss =[]
        #print(out.fit_report(min_correl=10))
        sigma = out.params['g1_sigma'].value
        amplitude = out.params['g1_amplitude'].value
        sigma_list.append(sigma); amplitude_list.append(amplitude)
        fit_params = {}

        #gauss_fit_parameters = [out.params[key].value for k in out.params]
        #print(key, "=", out.params[key].value, "+/-", out.params[key].stderr)
        gauss_fit_parameters = []

    return sigma_list, amplitude_list
