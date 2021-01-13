import numpy as np
from scipy.interpolate import splev
from scipy.interpolate import splrep
import matplotlib.pyplot as plt
from scipy.optimize import bisect
from scipy.misc import derivative

Re = np.array([0.2, 2, 20, 200, 2000, 20000])
Cd = np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433])

tck = splrep(Re, Cd, s=0)

Re_new = np.arange(0.2, 20000, 0.1)
Cd_new = splev(Re_new, tck, der=0)

plt.figure()
plt.loglog(Re, Cd, 'o', Re_new, Cd_new, '-')

plt.show()
