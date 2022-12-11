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
fig, ax = plt.subplots(1, 2, figsize=(
    30*ps.cm, 20*ps.cm), sharex=True, sharey=True)

for i, cond in enumerate(np.unique(data.cat)):

    for name in np.unique(data.subj):

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
        ax[i].plot(x, y, 'o', label='_')
        ax[i].plot(
            x_fit, y_fit, label=f"{name} thresh = {np.round(thresh, 2)}")

        # plot the threshold
        ax[i].plot([thresh, thresh], [0.25, threshy], lw=1,)
ax[0].legend()
ax[1].legend()
plt.show()
