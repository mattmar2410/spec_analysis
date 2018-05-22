from becquerel import Spectrum
import os
from copy import deepcopy
import numpy as np

fname = 'digibase_5min_30_1.Spe'

def fix_spe_zero_cal(fname, fname_new=None):
    if fname_new is None:
        fname_new = '{}_fixed{}'.format(*os.path.splitext(fname))
    with open(fname, 'r') as infile:
        old_lines = [l.rstrip('\n') for l in infile]
    new_lines = deepcopy(old_lines)
    for i, l in enumerate(old_lines):
        if l.startswith('$ENER_FIT'):
            cal = [float(x) for x in old_lines[i + 1].split()]
            if np.isclose(sum(cal), 0.):
                new_lines[i + 1] = '1.0 1.0'
                print('Fixed line:', i + 2)

    with open(fname_new, 'w') as infile:
        infile.write('\n'.join(new_lines) + '\n')

    return fname_new

spec_1 = Spectrum.from_file(fix_spe_zero_cal(fname))
