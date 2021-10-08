# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:38:31 2021

@author: anonymous
d(s+s ) = m*lambda

"""




D_GRATING = 1/(600*1000) # m /groove
T_peak = 192.54e12

c = 299792458

import numpy as np
import pandas as pd
import icecream as ic
import os

lam =c/T_peak
s= 1*lam/D_GRATING
c= np.sqrt(1-s**2)

katamuki = 1+c