from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

from modules.functions import bound_logistic
from modules.prepro import prepro


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


# run preprocessing
dataroot = Path("../data/4afc")
processed_dataroot = Path('../data_processed')
prepro(dataroot, processed_dataroot)

# load dataset
data = pd.read_csv(f"../data_processed/4afc_all.csv")

# make a logistic function for fitting
logistic = bound_logistic(0.25, 1)

# iterate through all in both categories and collect thresholds
conds, names, threshs = [], [], []

# iterate through conditions (high and low) and through subjects
for condition in np.unique(data.cat):
    for i, name in enumerate(np.unique(data.subj)):

        # get data for this name
        x = np.asanyarray(data.what[(data.cat == condition) & (
            data.subj == name)], dtype=np.float64)
        y = np.asanyarray(data.prop[(data.cat == condition) & (
            data.subj == name)], dtype=np.float64)

        # fit the logistic function
        popt, pcov = curve_fit(logistic, x, y, method="trf", maxfev=50000)

        # make the model curve
        x_fit = np.arange(0, 0.12, 0.001)
        y_fit = logistic(x_fit, *popt)

        # get threshold value
        thresh = x_fit[y_fit == find_nearest(y_fit, 0.625)][0]

        # append current condition and threshold
        conds.append(condition)
        names.append(name)
        threshs.append(thresh)

# make a dataframe
dthresh = pd.DataFrame(np.asarray(
    [np.asarray(conds), np.asarray(names), np.asarray(threshs)]).T, columns=('cond', 'name', 'thresh'))

# save dataframe to data_processed
dthresh.to_csv(f'{processed_dataroot}/4afc_thresholds.csv')
