# coding: utf-8
def integral(f, a, b):
    import numpy as np
    x = np.linspace(a, b, num=10000, endpoint=True)
    y = f(x)
    gfg = np.trapz(y, x)
    return gfg
