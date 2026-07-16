import numpy as np
import pandas as pd
import importlib
import fourDEnVar_engine
importlib.reload(fourDEnVar_engine)

if __name__=="__main__":

    Xb=np.genfromtxt("linear_tests/Xb.dat")
    hX=np.genfromtxt("linear_tests/HX.dat")
    y=np.genfromtxt("linear_tests/y.dat")
    R=np.genfromtxt("linear_tests/R.dat")
    hx_bar=np.genfromtxt("linear_tests/Hxbar.dat")
    
    x=fourDEnVar_engine.fourDEnVar_engine(Xb, hX, y, R, hx_bar)
    xa=x.xa
    Xa=x.Xa

    print(xa)
    print(Xa)
