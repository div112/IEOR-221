#!/usr/bin/env python
# coding: utf-8

## This is the American call option pricer along with the Greeks calculator.







import numpy as np
from scipy.stats import norm


# In[79]:


def call_pricer(n, S, K, r,q, v, t):  
##for american Call option

    dt = t/n 

    u = np.exp(v*np.sqrt(dt))

    d = 1/u

    p = (np.exp((r-q)*dt)-d) / (u-d) 
    #For the binom price tree
    val = np.zeros((n+1,n+1))
    val[0,0] = S
    for i in range(1,n+1):
        val[i,0] = val[i-1,0]*u
        for j in range(1,i+1):
            val[i,j] = val[i-1,j-1]*d           
    # final node   
    optionvalue = np.zeros((n+1,n+1))
    for j in range(n+1):
            optionvalue[n,j] = max(0, val[n,j]-K)
    #backward calc
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            optionvalue[i,j] = max(0, val[i,j]-K, np.exp(-r*dt)*(p*optionvalue[i+1,j]+(1-p)*optionvalue[i+1,j+1]))

    return optionvalue[0,0]


# In[80]:


print("Value of American Call option is:", call_pricer(100, 100, 100, 0.02, 0.08, 0.35, 1))


# In[ ]:





# In[81]:


def greeks(n, S, K, r,q, v, t):  
##for american Call option

    dt = t/n 

    u = np.exp(v*np.sqrt(dt))

    d = 1/u

    p = (np.exp((r-q)*dt)-d) / (u-d) 
    #For the binom price tree --> s
    val = np.zeros((n+1,n+1))
    val[0,0] = S
    for i in range(1,n+1):
        val[i,0] = val[i-1,0]*u
        for j in range(1,i+1):
            val[i,j] = val[i-1,j-1]*d  
    # final node  --> f 
    optionvalue = np.zeros((n+1,n+1))
    for j in range(n+1):
            optionvalue[n,j] = max(0, val[n,j]-K)
    #backward calc
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            optionvalue[i,j] = max(0, val[i,j]-K, np.exp(-r*dt)*(p*optionvalue[i+1,j]+(1-p)*optionvalue[i+1,j+1]))

    Delta= (optionvalue[1,0]- optionvalue[1,1])/(val[1,0]- val[1,1])
    d2= (optionvalue[2,0] - optionvalue[2,1])/(val[2,0]- val[2,1])
    d1= (optionvalue[2,1]- optionvalue[2,2])/(val[2,1]- val[2,2])
    Gamma= (d2-d1)/ (val[2,1]- val[2,2])
    Theta= (optionvalue[2,1]- optionvalue[0,0])/(0.02)

    return Delta, Gamma, Theta


# In[82]:


greeks_1= greeks(100, 100, 100, 0.02, 0.08, 0.35, 1)


# In[83]:


Vega = (call_pricer(100, 100, 100, 0.02, 0.08, 0.36, 1)- call_pricer(100, 100, 100, 0.02, 0.08, 0.35, 1))/ 0.01
Vega


# In[84]:


Rho= (call_pricer(100, 100, 100, 0.03, 0.08, 0.35, 1)- call_pricer(100, 100, 100, 0.02, 0.08, 0.35, 1))/ 0.01
Rho


# In[85]:


print("Price of the American Call option is: ", call_pricer(100, 100, 100, 0.02, 0.08, 0.35, 1))
print("Delta is equal to: ", greeks_1[0])
print("Gamma is equal to: ", greeks_1[1])
print("Theta is equal to: ", greeks_1[2])
print("Vega is equal to: ", Vega )
print("Rho is equal to: ", Rho)


# In[ ]:





# In[ ]:





# In[ ]:




