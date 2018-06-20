import numpy as np
import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit
#from modelling import gauss
import statsmodels.api as sm
from lmfit.models import GaussianModel
from lmfit.models import LinearModel
from sys import argv

def man_calibration(channel_data, cnts_data, energy_list, range_data):

    '''
    man_calibration(energy_data, cnts_data, energy_list, range)
    Returns two arrays that should be used with becquerel for linear calibration
    analog_cal = bq.LinearEnergyCal.from_points(chlist=channel_number, kevlist=energies)
    It is a manual input using a graph of channel_number vs cpskev_vals

    energy_data: .energies_kev that has been calibrated from becquerel
    cnts_data: .cps_vals from becquerel spectrum
    range: is the counts data to be calibrated. Use becquerels .cps_vals function
    enter the channel number ranges that you want the function to find the maximum
    counts and position from
    '''
    channel_max_list = []; i = 0
    for channel in range_data:
        if i%2 == 0:
            i+= 1
            channel_old = channel
        else:
            x_loc = list(filter(lambda x:(channel_old)<channel_data[x]<(channel),range(len(channel_data))))
            #x_loc_pk = range(int(x_loc-5), int(x_loc[0]+5))
            pk_cnt = np.argmax(cnts_data[x_loc])
            channel_max_list.append(x_loc[pk_cnt])
            channel_old = channel
            i += 1

    '''
    sorting channel number so the correct channel number corresponds with
    the correct energy.
    '''
    channel_number = sorted(channel_max_list, key=int)
    energies = sorted(energy_list, key=int)

    return channel_number, energies
