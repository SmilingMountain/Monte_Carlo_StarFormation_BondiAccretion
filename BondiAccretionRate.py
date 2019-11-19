# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Calculates and plots the Bondi accretion rate for various types of interstellar gas

import numpy as np
import matplotlib.pyplot as plt
from astropy.constants import M_sun


M=np.logspace(-2,1,100)
density=[10**4,10**2,1,10**(-2)]
soundspeed=[10**(-1),1,10,10**2]

Msun=1*M_sun
print(Msun)
case_names=['cloud core','molecular cloud','diffuse atomic gas','diffuse X-ray gas']

for i in range(4):
    rho=density[i]
    cs=soundspeed[i]
    Mdot=1.4*(10**11)*(M**2)*(rho*1.6726219)*((cs/10)**(-3))/(Msun.cgs/(365.25*24*3600*10**6))
    plt.plot(M,Mdot,label=case_names[i])

#plt.axis([10**(-2),10,10**(-16),10**2])
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.title('Bondi accretion rate')
plt.xlabel('Object mass / $M_\odot$')
plt.ylabel('Accretion rate / $M_\odot$ $Myr^{-1}$')
filename='bondi_accretion'
plt.savefig(filename)
plt.show()
plt.close()

