import os
from copy import deepcopy
import numpy as np

def fix_spe(fname, fname_new=None):
    '''
    fix_spe_zero_cal(fname, fname_new=None) creates a new file name for an uncalibrated
    gammavision spectrum
    fname: the spectrum that needs to be calibrated
    '''
    if fname_new is None:
        fname_new = '{}_fixed{}'.format(*os.path.splitext(fname))
    with open(fname, 'r') as infile:
        old_lines = [l.rstrip('\n') for l in infile]
    new_lines = deepcopy(old_lines)
    for i, l in enumerate(old_lines):
        if l.startswith('$MCA_CAL'):
            cal = [float(x) for x in old_lines[i + 2].split()]
            if np.isclose(sum(cal), 0.):
                new_lines[i + 2] = '1.0 1.0 1.0'
                print('Fixed line:', i + 2)

    with open(fname_new, 'w') as infile:
        infile.write('\n'.join(new_lines) + '\n')

    return fname_new
