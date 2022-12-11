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

def getindex(df):

    mean = []
    sem = []
    names = []
    for name in np.unique(df.subj):
        print(np.min(df.strat_idx[df.subj==name]))
        print(np.max(df.strat_idx[df.subj==name]))
        mean.append(np.mean(df.strat_idx[df.subj==name]))
        sem.append(np.std(df.strat_idx[df.subj==name]))
        names.append(name)

    return mean, sem, names

if __name__ == "__main__":
    
    # import the data
    dataroot = Path("../data/cvs")
    processed_dataroot = Path("../data_processed")
    df = dataimport(dataroot, processed_dataroot)
    colors = mcolors.TABLEAU_COLORS

    mean, sem, names = getindex(df)

    fig, ax = plt.subplots()

    for i, name in enumerate(names):
        plt.errorbar(mean[i], i, xerr=sem[i], fmt='bo')

    ax.set_xlim(0,1)

    plt.show()
