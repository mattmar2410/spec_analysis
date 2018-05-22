import numpy as np
import matplotlib.pyplot as plt
from lmfit.models import GaussianModel
from lmfit.models import LinearModel

def plot_gauss(energy_data, cnts_data, energy_spectrum, channel_width):
    '''
    plot_gauss takes an input spectrum and plots the gaussian fit to the photopeaks
    Make sure the spectrum is calibrated first.
    plot_gauss(energy_data, cnts_data, energy_spectrum, channel_width)
    energy_data: .energies_kev that has been calibrated from becquerel
    cnts_data: .cps_vals from becquerel spectrum
    energy_spectrum: an array of gamma energies generated from gamma_energies
    channel_width: width of the peak for analysis purposes
    '''
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

        plt.figure()
        plt.plot(x,real_y)
        plt.plot(x, out.best_fit, 'k--')
        energy_title = np.argmax(x)
        max_y = np.argmax(real_y)  # Find the maximum y value
        max_x = x[(max_y)]  # Find the x value corresponding to the maximum y value
        plt.title('Gaussian fit around %0.1f keV' % x[max_y])
        plt.xlabel('Energy (keV)')
        plt.ylabel('CPS')
        plt.show()
        gauss_x = []; gauss_y = []; parameter_list_1 = []
        real_y_gauss =[]
