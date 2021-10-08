# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 16:11:45 2020

レンズの公式
1       1       1
-  +    -   =   -
S1      S2      F


@author: anonymous
"""

import numpy as np
from scipy import optimize
F=17.3 #焦点距離
S1 =60



def f(_S2):
    sahen=1/S1+1/_S2
    uhen=F**-1
    return sahen-uhen

S2=optimize.fsolve(f,40) #突っ込む関数，　近辺探索の初期値
print(S2)