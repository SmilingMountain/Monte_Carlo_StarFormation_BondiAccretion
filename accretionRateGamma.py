# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 23:06:19 2017

@author: ai15aax
"""

# Accretion rate for specific gamma

from astropy.constants import G,M_sun
import astropy.units as u 
import numpy as np

Msun=1*M_sun
rhoinf=10**(-24)*(u.g)*(u.cm)**(-3)
cs=10*(u.km)*(u.s)**(-1)

x=1.4 # gamma
f=(2/(5-3*x))**((5-3*x)/(2*x-2))

Mdot=f*np.pi*(G**2)*(Msun**2)*rhoinf/(cs**3)

print('\n Mdot =', Mdot.cgs)