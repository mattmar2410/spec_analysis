from lmfit.models import QuadraticModel
import numpy as np
import matplotlib.pyplot as plt
import operator

def fit_nrg_resolution(sigma, Energy):
    '''
    fit = fit_nrg_resolution(sigma, Energy)
    **Energy must be the same energy list used for spectrum_gauss_fit
    **otherwise the energy and sigma values will not correspond
    Returns the quadratic fit to the Energy vs sigma plot
    sigma: generated from spectrum_gauss_fit
    Energy: generated from gamma_energies
    '''
    energy_channel = list(zip(sigma, Energy))
    energy_channel.sort(key=operator.itemgetter(1))
    sigma, Energy = zip(*energy_channel)
    model = QuadraticModel(prefix='q1_')
    pars = model.guess(sigma, x=Energy)
    pars.update(model.make_params())
    pars['q1_c'].set(0, 0)
    #pars['q1_'].set(x[np.argmax(real_y)], min=x[np.argmax(real_y)]\
    #- 3)
    out  = model.fit(sigma, pars, x=Energy)
    q1_a = out.params['q1_a'].value
    q1_b = out.params['q1_b'].value
    q1_c = out.params['q1_c'].value

    x_new = np.linspace(0, Energy[-1], 50)
    y_new = q1_a*(x_new)**2 + q1_b*(x_new) + q1_c
    plt.title("Energy Resolution")
    plt.xlabel("Energy (keV)")
    plt.ylabel("$\sigma$")
    plt.plot(x_new, y_new, 'k')
    plt.plot(Energy, sigma, 'o')
    fit = [q1_a, q1_b, q1_c]
    return fit
