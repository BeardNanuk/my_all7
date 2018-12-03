
# ze function for signal processing 
# created on Sat Sep 22 15:21:32 EDT 2018

import math as M
from future.utils import native
def next_pow_2(i):
    """
    Find the next power of two

    >>> int(next_pow_2(5))
    8
    >>> int(next_pow_2(250))
    256
    """
    # do not use NumPy here, math is much faster for single values
    buf = M.ceil(M.log(i) / M.log(2))
    return native(int(M.pow(2, buf)))



