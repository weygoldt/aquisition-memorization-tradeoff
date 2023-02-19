import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

from modules.functions import bound_logistic
from modules.plotstyle import PlotStyle


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


ps = PlotStyle()
logistic = bound_logistic(0.25, 1)

data = pd.read_csv('../data_processed/4afc_all.csv')

plt.rcParams["axes.prop_cycle"] = ps.get_cycle("tab20c")
fig, ax = plt.subplots(figsize=(12*ps.cm, 12*ps.cm), sharex=True, sharey=True, constrained_layout=True)

cond = 'high'
name = 'VP7'

# get data for this name
x = np.asanyarray(data.what[(data.cat == cond) & (
    data.subj == name)], dtype=np.float64)

y = np.asanyarray(data.prop[(data.cat == cond) & (
    data.subj == name)], dtype=np.float64)

# fit the logistic function
popt, pcov = curve_fit(logistic, x, y, method="trf", maxfev=50000)

# make the model curve
x_fit = np.arange(0, 0.12, 0.001)
y_fit = logistic(x_fit, *popt)

# find the threshold
thresh = x_fit[y_fit == find_nearest(y_fit, 0.625)][0]
threshy = y_fit[y_fit == find_nearest(y_fit, 0.625)][0]

# plot
ax.plot(x, y, 'o', label='_', c='darkgray')
ax.plot(x_fit, y_fit, label=f"{name} thresh = {np.round(thresh, 2)}", lw=2, c='k')

# plot the threshold
ax.plot([thresh, thresh], [0, threshy], lw=1.5, ls='dashed', c='k')
ax.plot([0, 0.12], [threshy, threshy], lw=2, c='lightgray', zorder = -1)
ax.plot([0, 0.12], [0.25, 0.25], lw=2, c='lightgray', zorder=-10)
ax.plot([0, 0.12], [1, 1], lw=2, c='lightgray', zorder=-10)

ax.text(0.078, 0.28, 'chance level')
ax.text(0.068, 0.66, 'perception level')

ax.set_xlabel('stimulus duration [s]')
ax.set_ylabel('proportion correct')
ax.set_ylim(0,1.1)
ax.set_xlim(0, 0.12)

from modules.functions import figsave

figsave('../figs/single_4afc_plot')
plt.show()