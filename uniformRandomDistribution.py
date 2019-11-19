# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:49:59 2017

@author: ai15aax
"""
import numpy.random as rnd
import numpy as np
import matplotlib.pyplot as plt

x=0.01*rnd.uniform(size=10000)
print(x)

a=plt.figure(1) # creating the log-log histogram:
counts,bin_edges=np.histogram(x,bins=np.logspace(-3,-2,50))
plt.hist(x,range=(-3.5,-1.5),bins=np.logspace(-3,-2,50),log=True)
plt.yscale('log')
plt.xscale('log')
bin_centres=(bin_edges[:-1]+bin_edges[1:])/2. # this calculates the x position of the error bars
err=np.sqrt(counts) # error from Poisson distribution
plt.errorbar(bin_centres,counts,yerr=err,fmt='x') # plotting the error bars
plt.xlabel("$M/M_\odot$")
plt.ylabel("Number of stars")
plt.title("Initial Mass Distribution")
plt.savefig("log_histogram") # saves with extension .png

b=plt.figure(2)
counts2,bin_edges2=np.histogram(x)
plt.hist(x)
bin_centres2=(bin_edges2[:-1]+bin_edges2[1:])/2. # this calculates the x position of the error bars
err2=np.sqrt(counts2) # error from Poisson distribution
plt.errorbar(bin_centres2,counts2,yerr=err2,fmt='x') # plotting the error bars
plt.xlabel("$M/M_\odot$")
plt.ylabel("Number of stars")
plt.title("Initial Mass Distribution")
plt.savefig("linear_histogram") # saves with extension .png           
           
plt.show() 

plt.close()    