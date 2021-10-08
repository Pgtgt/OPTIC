# -*- coding: utf-8 -*-
"""
Created on Sun May 17 19:59:44 2020
@author: wsxhi
"""

from optics import *
import pyqtgraph as pg
import numpy as np
from pyqtgraph import Point
c = 299792458
app = pg.QtGui.QApplication([])

w = pg.GraphicsWindow(border=0.5)  # 境界線の濃さ

d_Grate = 1.667e3  # nm/line

w.setWindowTitle(str(d_Grate))
w.resize(500, 500)
w.show()

view = w.addViewBox()
view.setAspectLocked()
grid = pg.GridItem()
view.addItem(grid)
# 表示範囲　適当でも変わらないleft, top, width, height
view.setRange(pg.QtCore.QRectF(-50, -50, 100, 100))

optics = []
optics_ = []
# rays1 = []
grate_width = 3
z0 = (50e-3)*10**3
l0 = (51e-3)*10**3
theta = 30
startwl = 1570-60/2
stopwl = 1570+60/2
centwl = (startwl+stopwl)/2  # Optical Path Difference の計算に使うようの波長
# d_Grate=2.2e3,  # nm

"""
光が当たる順番に定義
"""


g0 = Grating(r1=0, pos=(0.0, 50+grate_width/2), d=grate_width,
             angle=90, m=+1, d_Grate=d_Grate)  # 右へそれる設定
optics.append(g0)

l0 = Lens( glass='Corning7980',
          r1=6, r2=6, 
          d=4, 
          dia = 10
          
          
    )  # 右へそれる設定
optics.append(l0)

# g0_ = Grating(r1=0, pos=(0.0 ,50+grate_width/2), d=grate_width, angle=90,m=-1, d_Grate = d_Grate)#右へそれる設定
# optics_.append(g0_)
# g1 = Grating(r1=0, pos=(1.0 ,50+grate_width/2), d=grate_width, angle=90,m=+1, d_Grate = 1.0e3)#右へそれる設定
# optics.append(g1)

# g1_ = Grating(r1=0, pos=(1.5 ,50+grate_width/2), d=grate_width, angle=90,m=+1, d_Grate = 1.5e3)#右へそれる設定
# optics.append(g1_)

# g2 = Grating(r1=0, pos=(2.0 ,50+grate_width/2), d=grate_width, angle=90,m=+1, d_Grate = 2.0e3)#右へそれる設定
# optics.append(g2)

# g2_ = Grating(r1=0, pos=(2.5 ,50+grate_width/2), d=grate_width, angle=90,m=+1, d_Grate = 2.5e3)#右へそれる設定
# optics.append(g2_)

# g3 = Grating(r1=0, pos=(3.0 ,50+grate_width/2), d=grate_width, angle=90,m=+1, d_Grate = 3.0e3)#右へそれる設定
# optics.append(g3)

# g3_ = Grating(r1=0, pos=(3.5 ,50+grate_width/2), d=grate_width, angle=90,m=+1, d_Grate = 3.5e3)#右へそれる設定
# optics.append(g3_)

# g4 = Grating(r1=0, pos=(4.0 ,50+grate_width/2), d=grate_width, angle=90,m=+1, d_Grate = 4.0e3)#右へそれる設定
# optics.append(g4)

# g4_ = Grating(r1=0, pos=(4.5 ,50+grate_width/2), d=grate_width, angle=90,m=+1, d_Grate = 4.5e3)#右へそれる設定
# optics.append(g4_)

# g5 = Grating(r1=0, pos=(5.0 ,50+grate_width/2), d=grate_width, angle=90,m=+1, d_Grate = 5.0e3)#右へそれる設定
# optics.append(g5)

# g5_ = Grating(r1=0, pos=(5.5 ,50+grate_width/2), d=grate_width, angle=90,m=+1, d_Grate = 5.5e3)#右へそれる設定
# optics.append(g5_)

# g6 = Grating(r1=0, pos=(6.0 ,50+grate_width/2), d=grate_width, angle=90,m=+1, d_Grate = 6.0e3)#右へそれる設定
# optics.append(g6)

# g6_ = Grating(r1=0, pos=(6.5 ,50+grate_width/2), d=grate_width, angle=90,m=+1, d_Grate = 6.5e3)#右へそれる設定
# optics.append(g6_)

# g7 = Grating(r1=0, pos=(7.0 ,50+grate_width/2), d=grate_width, angle=90,m=+1, d_Grate = 7.0e3)#右へそれる設定
# optics.append(g7)

# m1 = Mirror(r1=0, pos=(100,0), d=5, angle=-90)
# optics.append(m1)

# b1 = Block(r1=0, pos=(l0*np.sin(theta*np.pi/180),z0-l0*np.cos(theta*np.pi/180)), d=1 , angle=-45)
# optics.append(b1)
# 吸収して，かつその座標を出せるようなBlockを作る
# l1 = Lens(r1=15, r2=15, d=6, angle=90, glass='Corning7980',pos=(0,50))
# optics.append(l1)

# allRays1 = []
allRays = []
# allRays_ = []

"""Rayに＋１　０等の値をねじ込む
回折格子関数Gratingをミラーパクッテ入れる　m1 = Mirror(r1=0, pos=(0,10), d=5, angle=90)
の設定でできるような関数が望ましい
"""
# r = Ray(dir=Point(0,1),start=Point(0,0)) #始点とベクトル　abs(dir)=1がいいのかね
# view.addItem(r)
# allRays.append(r)

for wl in np.linspace(startwl, stopwl, 5):
    # for hol in np.linspace(-5,5,2):
    # r = Ray(start=Point(0,0),dir=Point(0,1), wl=wl)
    r = Ray(start=Point(0, 0), dir=Point(0, 1), wl=wl)
    view.addItem(r)
    allRays.append(r)

# for wl in np.linspace(startwl,stopwl,10):
#     # for hol in np.linspace(-5,5,2):
#     # r = Ray(start=Point(0,0),dir=Point(0,1), wl=wl)
#     r_ = Ray(start=Point(0,0),dir=Point(0,1), wl=wl)
#     view.addItem(r_)
#     allRays_.append(r_)


# for f in np.linspace(190,195, 500):
#     r = Ray(start=Point(0,0),dir=Point(0,1), wl=( c / (f*10**12) )*10**9)
#     view.addItem(r)
#     allRays.append(r)

for o in optics:
    view.addItem(o)

# for o in optics_:
#     view.addItem(o)


t = Tracer(allRays, optics)
# t_= Tracer(allRays_, optics_)
# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()