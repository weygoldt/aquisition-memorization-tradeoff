import os
from pathlib import Path
from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

from modules.prepro import prepro

dataroot = Path("../data/test/4afc")
prepro(dataroot)

data = pd.read_csv(f"{dataroot}/4afc_all.csv")

x = data.what[data.cat == 'low']
y = data.prop[data.cat == 'low']


def f(x, a, b, c, d):
    return a / (1. + np.exp(-c * (x - d))) + b


popt, pcov = curve_fit(f, x, y, method="lm")

x_fit = np.linspace(min(x), max(x), 100)
y_fit = f(x_fit, *popt)

fig, ax = plt.subplots(1, 1, figsize=(6, 4))
ax.plot(x, y, 'o')
ax.plot(x_fit, y_fit, '-')
plt.show()
