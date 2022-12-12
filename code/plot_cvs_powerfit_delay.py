import os
from pathlib import Path

import cmocean
import cmocean.cm as cmo
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plottools.colors as clrs
import seaborn as sns
from matplotlib.pyplot import cm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
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

newcmap = cmocean.tools.crop_by_percent(cmo.ice, 20, which='max', N=None)
colors = newcmap(np.linspace(0, 1, 4))

newcmap = cmocean.tools.crop_by_percent(cmo.haline, 20, which='max', N=None)
colors2 = newcmap(np.linspace(0,1,4))


def plot_errorbars(df, ax, color):

    for name in df.names: 
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
df_0 = df[df.delay == 0]
df_2 = df[df.delay == 1.5]

ms_0 = mean_sem(df_0)
ms_2 = mean_sem(df_2)

popt0, pcov = curve_fit(func_powerlaw, ms_0.switches_means, ms_0.tpertrial_means, method="trf", maxfev=50000)
popt2, pcov = curve_fit(func_powerlaw, ms_2.switches_means, ms_2.tpertrial_means, method="trf", maxfev=50000)

fig, ax = plt.subplots(figsize=(12*ps.cm, 12*ps.cm))
plot_errorbars(ms_0, ax, color='red')
plot_errorbars(ms_2, ax, color='blue')

x = np.linspace(ms_2.switches_means.min()-0.4, ms_2.switches_means.max()+2, 1000)
ax.plot(x, func_powerlaw(x, *popt0))
ax.plot(x, func_powerlaw(x, *popt2))

axins = inset_axes(ax, 3, 2.5, loc=1)
plot_errorbars(ms_0, axins, color=colors[1])
plot_errorbars(ms_2, axins, color=colors[3])
axins.plot(x, func_powerlaw(x, *popt0), color=colors2[2], zorder=10)
axins.plot(x, func_powerlaw(x, *popt2), color=colors2[3], zorder=10)

x1, x2, y1, y2 = 3, 15, 1, 5
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
axins.tick_params(left=False, right=False, labelleft=False, labelbottom=False, bottom=False)
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

plt.show()
