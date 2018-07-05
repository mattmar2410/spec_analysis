import numpy as np
import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit
#from modelling import gauss
import statsmodels.api as sm
from lmfit.models import GaussianModel
from lmfit.models import LinearModel

def calibration(spectrum_data, energy_list, channel_width, clean_right):

    '''
    channel_number, energies = calibration(spectrum_data, energy_list, channel_width, clean_right)
    Returns two arrays that should be used with becquerel for linear calibration
    analog_cal = bq.LinearEnergyCal.from_points(chlist=channel_number, kevlist=energies)

    spectrum_data: is the counts data to be calibrated. Use becquerels .cps_vals function
    energy_list: is generated using gamma_energies included in this package
    channel_width: how wide the peak of interest is. the code will use this command and turn the
    peak to zero after it locates its maximum
    clean_right: removes background information so the code only finds peaks of interest. There
    needs to be some knowledge of the spectrum before calibration can be performed
    '''

    list_data = np.array(spectrum_data).tolist()
    iterator = 0
    while iterator < (clean_right):
        list_data[iterator] = 0
        iterator += 1
    '''
    merging the data for the calibration
    Also converting merged data into a list so channels can be
    removed easier.
    '''
    data_2_calibrate = list_data
    i = 0; channel_max_list = []; gauss_x = []; gauss_y = []
    fit_channel = []
    while i < len(energy_list):
        channel_max = np.argmax(data_2_calibrate)
        data_left = channel_max - channel_width
        data_right = channel_max + channel_width
        channel_max_list.append(channel_max)
        iterator = data_left
        while iterator < (data_right):
            data_2_calibrate[iterator] = 0
            iterator += 1
        i += 1

    '''
    sorting channel number so the correct channel number corresponds with
    the correct energy.
    '''
    channel_number = sorted(channel_max_list, key=int)
    energies = sorted(energy_list, key=int)

    return channel_number, energies
