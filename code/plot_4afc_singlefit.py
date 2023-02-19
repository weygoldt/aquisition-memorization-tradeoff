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
from scipy.optimize import curve_fit
from scipy.stats import wilcoxon

from modules.functions import bound_logistic, figsave
from modules.plotstyle import PlotStyle

# init standardized plotstyle
ps = PlotStyle()


def find_nearest(array, value):
    """Like numpy-where but flexible"""
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx] 

def find_nearest_idx(array, value):
    """Like numpy-where but flexible"""
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

logistic = bound_logistic(0.25, 1) # logistic bound between chance lvl and 1

data = pd.read_csv('../data_processed/4afc_all.csv') # load 4afc data


names = [] # append names here
conds =  [] # append condition here
fits = [] # append fitted curve here
threshs = [] # append thresh from logistic fit here
exclude = [] # append exclude index here

for it, condition in enumerate(np.unique(data.cat)):

    # define colors for each subject
    color = iter(cm.rainbow(np.linspace(0, 1, 8)))

    # compute thresholds and exclude where threshold is out of range
    for i, name in enumerate(np.unique(data.subj)):

        # get data for this subject
        x = np.asarray(data.what[(data.cat == condition)&(data.subj == name)], dtype=float)
        y = np.asarray(data.prop[(data.cat == condition)&(data.subj == name)], dtype=float)

        # fit the logistic function to get a psychometric curve
        popt, pcov = curve_fit(logistic, x, y, method='trf', maxfev=100000)

        # make the model curve
        x_fit = np.arange(0, 0.14, 0.0001)
        y_fit = logistic(x_fit, *popt)

        # extract threshold (where detection is half of non-chance range)
        thresh = np.round(x_fit[y_fit == find_nearest(y_fit,0.625)][0], 3)
        thresh_y = y_fit[y_fit == find_nearest(y_fit,0.625)][0]

        if (thresh>0.1) or (thresh<0.01667):
            exclude.extend([1])
            names.append(name)
            fits.append(y_fit)
            conds.append(condition)
            threshs.append(thresh)
        else:
            exclude.extend([0])
            names.append(name)
            fits.append(y_fit)
            conds.append(condition)
            threshs.append(thresh)

# make a dataframe from the collected data
exclude = np.asanyarray(exclude, dtype=bool)
names = np.asarray(names, dtype=str)
fits = np.asarray(fits, dtype=float)
conds = np.asarray(conds, dtype=str)
threshs = np.asarray(threshs, dtype=float)

# make exclude for both levels
for name in np.unique(names):
    if 1 in exclude[names==name]:
        exclude[names==name] = 1

dthresh = pd.DataFrame(np.asarray([names, exclude, conds, threshs], dtype=object).T, columns=('name', 'exclude', 'cond', 'thresh'))
dthresh = dthresh.astype({"name": str, "exclude": bool, "cond": str, "thresh": float})

fig, ax = plt.subplots(figsize=(12*ps.cm,12*ps.cm), constrained_layout=True)

x = x_fit
x_stim = x_fit[(x_fit<0.1)&(x_fit>0.01667)]
newcmap = cmocean.tools.crop_by_percent(cmo.ice, 20, which='max', N=None)


color = newcmap(np.linspace(0, 1, 6))
for index in dthresh.index[dthresh.cond == cond]:

        fit = fits[index]
        fit_stim = fits[index][(x_fit<0.1)&(x_fit>0.01667)]
        
        if dthresh.exclude[index] == True:
            zorder = -10
            ax[i].plot(x, fit, c='lightgray', lw=2.5, zorder=zorder)
            ax[i].plot([dthresh.thresh[index], dthresh.thresh[index]], [0.25, find_nearest(fit, 0.625)], lw=1, c='lightgray', ls='dashed', zorder=zorder)
            ax[i].plot([dthresh.thresh[index]], [find_nearest(fit, 0.625)], marker='o', c='lightgray', zorder=zorder, markersize=7.5)
            
        else: 
            #c = next(color)
            c = color[ic]
            ax[i].plot(x, fit, lw=2.5, c=c, ls='dashed', zorder=-1)
            ax[i].plot(x_stim, fit_stim, lw=2.5, c=c, zorder=1)
            ax[i].plot([dthresh.thresh[index], dthresh.thresh[index]], [0.25, find_nearest(fit, 0.625)], lw=1, c=c)
            ax[i].plot([dthresh.thresh[index]], [find_nearest(fit, 0.625)], marker='o', c=c, markersize=7.5)
            ic += 1


ax[1].text(0, 0.9, '2 cpd')
ax[0].text(0, 0.9, '8 cpd')
ax[1].set_ylim(0.25, 1)
ax[0].set_ylim(0.25, 1)
ax[0].set_ylabel('proportion correct')
ax[0].set_xlabel('stimulus duration [s]')
ax[1].set_xlabel('stimulus duration [s]')

# remove the invalid datasets
dthresh_valid = dthresh[dthresh["exclude"] == False]

# plot pointplot
sbp = sns.pointplot(x = 'cond', y = 'thresh', hue='name', data = dthresh_valid, palette=color, ax=ax[2])
ax[2].set_xlabel('stimulus')
ax[2].set_ylabel('perception threshold [s]')

# set ticklabels, remove legends
ax[2].set_xticklabels(['8 cpd', '2 cpd'])
plt.legend([],[], frameon=False)

# save
figsave('4afc_psychofit')
plt.show()