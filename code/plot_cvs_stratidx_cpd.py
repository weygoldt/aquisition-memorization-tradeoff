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
    #mean = mean - mean.min()

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

    fig, ax = plt.subplots(figsize=(12*ps.cm, 12*ps.cm), constrained_layout=True)

    newcmap = cmocean.tools.crop_by_percent(cmo.ice, 40, which='both', N=None)
    colors1 = newcmap(np.linspace(0,1,9))
    newcmap = cmocean.tools.crop_by_percent(cmo.algae_r, 40, which='both', N=None)
    colors2 = newcmap(np.linspace(0,1,9))

    data = getindex(df[df.cpd == 8])
    newdata = data.sort_values(by=['mean'], ascending=True).reset_index()
    for i, name in enumerate(newdata.name):
        plt.errorbar(newdata['mean'][i], i, xerr=newdata['sem'][i], fmt='o', c=colors1[i], capsize=3, label='8 cpd'if i == 6 else "")
    
    data = getindex(df[df.cpd == 2])
    newdata = data.sort_values(by=['mean'], ascending=True).reset_index()
    for i, name in enumerate(newdata.name):
        plt.errorbar(newdata['mean'][i], i+0.3, xerr=newdata['sem'][i], fmt='o', c=colors2[i], capsize=3, label='2 cpd' if i == 6 else "")

    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    ax.get_yaxis().set_ticks([])
    ax.set_xticks(np.arange(-3.5, -0.4, 0.5))
    ax.spines.bottom.set_bounds(-3.5, -0.5)

    plt.text(0.05, 0.02, 'aqu.', fontsize=14, transform=plt.gcf().transFigure)
    plt.text(0.86, 0.02, 'mem.', fontsize=14, transform=plt.gcf().transFigure)

    ax.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", borderaxespad=0, ncol=3)
    ax.set_ylabel('subjects')
    ax.set_xlabel('strat. index')
    figsave('stratidx_cpd')
    plt.show()