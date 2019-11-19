# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:30:35 2017

@author: ai15aax
"""

import numpy.random as rnd
import numpy as np
import matplotlib.pyplot as plt

in_string1=input('Number of stars= ')
n=int(in_string1)
in_string2=input('Timestep in years= ')
dt=float(in_string2)

M=0.01*rnd.uniform(size=n) # random generation function for core masses
print('\n Initial mass distribution=',M)

T=3*10**6 # total accretion time (years)
cs=0.1 # sound speed (km/s)
#rho=1.6*10**(-20) # initial density (constant) (g/cm^3)

# implementation of random density generation:
rho_max=10**(-20)
rho=10.**rnd.normal(size=n)*rho_max

N=int(T/dt)

Sum=[]
limit=150. # maximum accretion limit in solar masses
print('\n Generating stellar cluster...')   

for i in range(n):
    mass=M[i]
    density=rho[i] # this is uncommented when using the random density generation
    for j in range(N):
        # rate of accretion calculation in solar masses/year (mass dependent):
        Mdot=1.4*(10**11)*(mass**2)*(density/(10**(-24)))*((cs/10)**(-3))/((1.989*10**33)/(365.25*24*3600))
        # accretion:
        dM=Mdot*dt
        mass=mass+dM
        if mass>limit:
           mass=150.
    Sum.append(mass)

a=plt.figure(1) # creating the log-log histogram:
ax  = a.add_subplot(111) # adding a subplot for plotting 1/M on the same graph
# now plot
counts,bin_edges=np.histogram(Sum,bins=np.logspace(-3,2.5,30))
ax.hist(Sum,range=(-3.5,2.5),bins=np.logspace(-3,2.5,30),log=True)
x = np.logspace(-3,2.5,30)
alpha=31.6 # proportionality constant 
f=alpha*(1/x)
h = ax.plot(x, f) # plotting 1/M
    
plt.yscale('log')
plt.xscale('log')
bin_centres=(bin_edges[:-1]+bin_edges[1:])/2. # this calculates the x position of the error bars
err=np.sqrt(counts) # error from Poisson distribution
plt.errorbar(bin_centres,counts,yerr=err,fmt='x') # plotting the error bars
plt.xlabel("$M/M_\odot$")
plt.ylabel("Number of stars")
plt.title("Final Mass Distribution")
plt.savefig("log_histogram_final") # saves with extension .png 

b=plt.figure(2)
axx  = b.add_subplot(111)
counts2,bin_edges2=np.histogram(Sum)
axx.hist(Sum)
y=np.setdiff1d(np.linspace(0,150,100),[0]) #to remove the zero
ff=1/y
hh = axx.plot(y, ff)

bin_centres2=(bin_edges2[:-1]+bin_edges2[1:])/2. # this calculates the x position of the error bars
err2=np.sqrt(counts2) # error from Poisson distribution
plt.errorbar(bin_centres2,counts2,yerr=err2,fmt='x') # plotting the error bars
plt.xlabel("$M/M_\odot$")
plt.ylabel("Number of stars")
plt.title("Final Mass Distribution")
plt.savefig("linear_histogram_final") # saves with extension .png

plt.show() 

plt.close()

print('\n Stellar cluster done.')   
