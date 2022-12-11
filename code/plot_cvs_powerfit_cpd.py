
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

# init standardized plotstyle
ps = PlotStyle()

# import the data
dataroot = Path("../data/cvs")
processed_dataroot = Path("../data_processed")
df = dataimport(dataroot, processed_dataroot)
colors = mcolors.TABLEAU_COLORS


def plot_errorbars(df, ax, color):

    for name, _ in zip(df.names, colors):
        minidf = df[df.names == name]
        ax.errorbar(
            minidf.switches_means,
            minidf.tpertrial_means,
            xerr=minidf.switches_sems,
            yerr=minidf.tpertrial_sems,
            fmt="o",
            label=name,
            color=color,
        )


# sort dataset by delay condition
df_0 = df[df.cpd == 2]
df_2 = df[df.cpd == 8]

ms_0 = mean_sem(df_0)
ms_2 = mean_sem(df_2)

popt0, pcov = curve_fit(func_powerlaw, ms_0.switches_means, ms_0.tpertrial_means, method="trf", maxfev=50000)
popt2, pcov = curve_fit(func_powerlaw, ms_2.switches_means, ms_2.tpertrial_means, method="trf", maxfev=50000)

fig, ax = plt.subplots()
plot_errorbars(ms_0, ax, color='red')
plot_errorbars(ms_2, ax, color='blue')

x = np.linspace(ms_2.switches_means.min()-0.4, ms_2.switches_means.max()+2, 1000)
ax.plot(x, func_powerlaw(x, *popt0))
ax.plot(x, func_powerlaw(x, *popt2))

plt.show()
