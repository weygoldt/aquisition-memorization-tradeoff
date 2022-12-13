import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from modules.functions import figsave
from modules.plotstyle import PlotStyle

ps = PlotStyle()

threshs = pd.read_csv('../data_processed/4afc_thresh.csv')

meanthresh = []
names =  []
for name in threshs.name:
    subdf = threshs[threshs.name == name]
    meanthresh.append(subdf.thresh.mean())
    names.append(name)

stratidxs = pd.read_csv('../data_processed/stratidx.csv')
strat = []
for name in names:
    subdf = stratidxs[stratidxs.name == name]
    strat.append(np.mean(subdf['mean']))

print(len(names))
print(len(meanthresh))
print(len(strat))

fig, ax = plt.subplots(figsize=(12*ps.cm, 12*ps.cm), constrained_layout=True)
ax.plot(strat, meanthresh, 'o')
ax.set_xlabel('strat. index')
ax.set_ylabel('mean detection threshold')
figsave('cvs_vs_4afc')
plt.show()