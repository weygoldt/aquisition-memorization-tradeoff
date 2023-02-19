import cmocean
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from modules.functions import figsave
from modules.plotstyle import PlotStyle

ps = PlotStyle()

threshs = pd.read_csv('../data_processed/4afc_thresh.csv')

meanthresh = []
names =  []
for name in np.unique(threshs.name):
    subdf = threshs[threshs.name == name]
    meanthresh.append(subdf.thresh.mean())
    names.append(name)

stratidxs = pd.read_csv('../data_processed/stratidx.csv')
strat = []
for name in names:
    subdf = stratidxs[stratidxs.name == name]
    strat.append(np.mean(subdf['mean']))

print(names)
print(meanthresh)
print(strat)
print(len(names))
print(len(strat))
print(len(meanthresh))

fig, ax = plt.subplots(figsize=(12*ps.cm, 12*ps.cm), constrained_layout=True)
names = np.asarray(names)
strat = np.asarray(strat)
meanthresh = np.asarray(meanthresh)


newcmap = cmocean.tools.crop_by_percent(cmocean.cm.ice, 20, which='max', N=None)
color = newcmap(np.linspace(0, 1, 6))

for i, name in enumerate(names):

    ax.plot(meanthresh[names==name],strat[names==name],  'o', color=color[i])
    print([names==name])
    print(strat[names == name])
    print(meanthresh[names == name])

#ax.plot(strat, meanthresh)
ax.set_xlabel('mean detection threshold')
ax.set_ylabel('strategy index')
figsave('cvs_vs_4afc')
plt.show()