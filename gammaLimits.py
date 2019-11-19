# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 22:08:32 2017

@author: ai15aax
"""

# Calculates limits for gamma

import sympy as sp
from sympy.abc import x

f=(2/(5-3*x))**((5-3*x)/(2*x-2))
gamma1=1
gamma2=5/3
print('\n For gamma=1, f=',sp.limit(f,x,gamma1)) 
print('\n For gamma=5/3, f=',sp.limit(f,x,gamma2)) 