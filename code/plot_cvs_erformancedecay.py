import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from modules.plotstyle import PlotStyle

ps = PlotStyle()

df = pd.read_csv('../data_processed/cvs.csv')

# commpute error rate per subject 
err = []
names = []
steps = []
step = int(len(np.unique(df.trialno))/5)
for name in np.unique(df.subj):
    for i in np.arange(step, len(df.index[df.subj == name])+step, step=step):
        
        #if i == step:
        #    err.append(np.nan)
        #    steps.append(0)
        #    names.append(name)
        
        num_true = len(df.iserror[df.subj == name][i-step : i][df.iserror[df.subj == name][i-step: i] == 1])
        errrate = 1-num_true/step
        err.append(errrate)
        steps.append(i-step/2)
        names.append(name)

err = np.asarray(err)
names = np.asarray(names)
steps = np.asarray(steps)
mean_err = [np.mean(err[steps==step]) for step in np.unique(steps)] 
mean_steps = np.unique(steps)

trialmean = df.groupby('trialno').mean()

fig, ax = plt.subplots(3,1, sharex=True, constrained_layout=True)
for i, name in enumerate(np.unique(df.subj)):
    ax[0].plot(df.trialno[df.subj == name], df.switches[df.subj == name], lw=1, c='gray')
    ax[1].plot(df.trialno[df.subj == name], df.tpertrial[df.subj == name], lw=1, c='gray')
    ax[2].plot(steps[names==name], err[names==name], lw=1, c='gray')


ax[0].plot(trialmean.index, trialmean.switches, lw=2, color='k')   
ax[1].plot(trialmean.index, trialmean.tpertrial, lw=2, color='k')
ax[2].plot(mean_steps, mean_err, lw=2, c='k')
ax[0].set_ylabel('# switches')
ax[1].set_ylabel('trial dur.')
ax[2].set_ylabel(f'prop. correct')
ax[2].set_xlabel('number of trials')


fig.align_labels()
from modules.functions import figsave

figsave('../figs/trial_stability')
plt.show()

