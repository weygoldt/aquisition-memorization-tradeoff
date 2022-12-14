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

from cvs_preprocessing import dataimport
from modules.functions import bound_logistic, figsave
from modules.plotstyle import PlotStyle
from plot_cvs_powerfit_all import func_powerlaw, mean_sem

# init standardized plotstyle
ps = PlotStyle()

def getindex(df):

    mean = []
    sem = []
    names = []
    for name in np.unique(df.subj):
        
        # get all data that survives the log transform
        data = np.log10(df.strat_idx[df.subj==name])[~np.isinf(np.log10(df.strat_idx[df.subj==name]))]
        m = np.mean(data)
        mean.append(np.mean(m))
        sem.append(np.std(data))
        names.append(name)

    sem = np.asarray(sem)
    mean = np.asarray(mean)

    # normalize by mean
    # mean = mean - mean.min()

    out = pd.DataFrame({'name': names,
        'mean': mean, 
        'sem': sem,
    })

    return out

if __name__ == "__main__":
    
    # import the data
    dataroot = Path("../data/cvs")
    processed_dataroot = Path("../data_processed")
    df = dataimport(dataroot, processed_dataroot)
    colors = mcolors.TABLEAU_COLORS

    data = getindex(df)
    newdata = data.sort_values(by=['mean'], ascending=True).reset_index()
    newdata.to_csv('../data_processed/stratidx.csv')

    fig, ax = plt.subplots(figsize=(12*ps.cm, 12*ps.cm), constrained_layout=True)

    newcmap = cmocean.tools.crop_by_percent(cmo.ice, 20, which='max', N=None)
    colors = newcmap(np.linspace(0,1,9))
    for i, name in enumerate(newdata.name):
        plt.errorbar(newdata['mean'][i], i, xerr=newdata['sem'][i], fmt='o', label=name, c=colors[i], capsize=3)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    #ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])
    ax.set_xticks(np.arange(-2, 1.6, 0.5))
    ax.spines.bottom.set_bounds(-2, 1.5)

    plt.text(0.07, 0.02, 'aqu. ⟵', fontsize=14, transform=plt.gcf().transFigure)
    plt.text(0.792, 0.02, '⟶ mem.', fontsize=14, transform=plt.gcf().transFigure)
    
    ax.set_ylabel('subjects')
    ax.set_xlabel('strat. index')
    figsave('stratidx')
    plt.show()
