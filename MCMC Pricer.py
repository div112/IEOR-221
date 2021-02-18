#!/usr/bin/env python
# coding: utf-8

# This uses Monte Carlo Markov Chain simulation to price options along with the antithetic sampling and control variate methods to price options. 


##importing libs
import math
import numpy
from numpy import *
from time import time


# In[79]:


random.seed(15000)
t0 = time()
# the necessary parameters for the BSM eq
# current stock price
S0 = 100.
#strike price
K = 100.
#time to maturity in years
T = 1.0; 
#rf rate ; volatility
r = 0.02; sigma = 0.35
#continuous dividend yield
q= 0.08
M = 100; dt = T / M; I = 2000



# In[80]:


##Price obtained using BSM formula
st_bsm= 10.56


# In[81]:


import numpy as np 
import scipy as sp 
def option_payoff(S, K, option_type):     
    payoff = 0.0     
    if option_type == "call":         
        payoff = max(S - K, 0)     
    elif option_type == "put":         
        payoff = max(K - S, 0)     
    return payoff 


# In[82]:


S0 = 100.0 
K = 100.0 
T = 1.0 
r = 0.02 
q = 0.08 
sigma = 0.35 
option_type = "call" 
n_steps = 100 
#number of steps 
sp.random.seed(7321) 
#make result reproducable 
n_simulation = 2000 
#number of simulation 
dt = T/n_steps 
sqrt_dt = np.sqrt(dt) 
payoff = np.zeros((n_simulation), dtype = float) 
step = range(0, int(n_steps), 1) 

for i in range(0, n_simulation):     
    ST = S0     
    for j in step[:-1]:         
        epsilon = sp.random.normal()         
        ST *= np.exp((r - q - 0.5*sigma*sigma)*dt + sigma*epsilon*sqrt_dt)     
        payoff[i] = option_payoff(ST, K, option_type) 
        
        
option_price1 = np.mean(payoff)*np.exp(-r*T) 
print(option_type + ' price = ', option_price1)
print("Error is:", st_bsm-option_price1)


# In[83]:


## Part a

#Simulating I paths with M time steps

S= S0 * exp(cumsum((r - q - 0.5 * sigma ** 2) * dt + sigma * math.sqrt(dt) * random.standard_normal((M + 1, I)), axis=0))
#MC estimator
C0 = math.exp(-r * T) * sum(maximum(S[-1] - K, 0)) / I


print('The European Option Value is: ', C0) 
print('Error is:', C0- st_bsm)


##first 20 paths 
import matplotlib.pyplot as plt
plt.plot(S[:, :20])
plt.grid(True)
plt.xlabel('Steps')
plt.ylabel('Index level')
plt.show()


# In[85]:


##Part b-- Antithetic Sampling


# In[86]:


#S1= S0 * exp(cumsum((r - q - 0.5 * sigma ** 2) * dt + sigma * math.sqrt(dt) * 
            #(-random.standard_normal((M + 1, I))), axis=0))
#MC estimator
#C1 = math.exp(-r * T) * sum(maximum(S1[-1] - K, 0)) / I
for i in range(0, n_simulation):     
    ST = S0     
    for j in step[:-1]:         
        epsilon = -sp.random.normal()         
        ST *= np.exp((r - q - 0.5*sigma*sigma)*dt + sigma*epsilon*sqrt_dt)     
        payoff[i] = option_payoff(ST, K, option_type) 
        
        
option_price2 = np.mean(payoff)*np.exp(-r*T) 
print(option_type + ' price = ', option_price2)
print("Error is:", st_bsm-option_price2)

#print('The European Option Value is: ', C1) 
#print('Error is:', C1- st_bsm)


# In[87]:


#plt.plot(S1[:, :20])
#plt.grid(True)
#plt.xlabel('Steps')
#plt.ylabel('Index level')
#plt.show()


# In[88]:


#control variate
beta= 0.5
expected_ST= S0* np.exp((r-q)*T)
for i in range(0, n_simulation):     
    ST = S0     
    for j in step[:-1]:         
        epsilon = sp.random.normal()         
        ST *= np.exp((r - q - 0.5*sigma*sigma)*dt + sigma*epsilon*sqrt_dt)     
        payoff[i] = option_payoff(ST, K, option_type) -  beta *(ST- expected_ST)
        
        
option_price3 = np.mean(payoff)*np.exp(-r*T) 
print(option_type + ' price = ', option_price3)
print("Error is: ", st_bsm - option_price3)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




