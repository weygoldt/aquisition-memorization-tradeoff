import os
from pathlib import Path

import cmocean.cm as cmo
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plottools.colors as clrs
import seaborn as sns
from matplotlib.pyplot import cm
from scipy.optimize import curve_fit
from scipy.stats import wilcoxon

from cvs_preprocessing import dataimport
from modules.functions import bound_logistic
from modules.plotstyle import PlotStyle
from plot_cvs_powerfit_all import func_powerlaw, mean_sem
from plot_cvs_stratidx_all import getindex

# init standardized plotstyle
ps = PlotStyle()

# import the data
dataroot = Path("../data/cvs")
processed_dataroot = Path("../data_processed")
df = dataimport(dataroot, processed_dataroot)
colors = mcolors.TABLEAU_COLORS

# repeat for two categories
fig, ax = plt.subplots()

mean, sem, names = getindex(df[df.cpd==2])

for i, name in enumerate(names):
    plt.errorbar(mean[i], i, xerr=sem[i], fmt='bo')


mean, sem, names = getindex(df[df.cpd==8])

for i, name in enumerate(names):
    plt.errorbar(mean[i], i+0.2, xerr=sem[i], fmt='ro')

ax.set_xlim(0,1)

plt.show()