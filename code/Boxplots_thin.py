import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import cmocean

#from analysis3.0 import resp_time, shifts, proc_time, error_rate

#testdf = pd.DataFrame({'levels1': [0,0,1,1], 'levels2': [2,8,2,8], 'data': [0.1, 0.2, 0.3, 0.4]})
#sns.catplot(x='levels2', y='data', hue='levels1', data=testdf, kind='bar')
#plt.show()

error_rate = pd.read_csv('error_rate.csv', header=0)
#error_rate.drop(["NaN"], inplace=True)
resp_time = pd.read_csv('resp_time.csv', header=0)
#resp_time.drop(["NaN"], inplace=True)
proc_time = pd.read_csv('proc_time.csv', header=0)
#proc_time.drop(["NaN"], inplace=True)
shifts = pd.read_csv('shifts.csv', header=0)
#shifts.drop(["NaN"], inplace=True)

# a colormap can be accessed like this
colors = cmocean.cm.haline

# but this is only good for plotting continuous things, like heatmaps
# we need categories of colors! We need to discretize it!

# step 1: Cut off maxima and minima of colormap (because too bright or too dark)
new_colors = cmocean.tools.crop_by_percent(cmocean.cm.ice, 80, which='both')

# step 2: Make N discrete colors
N = 2 # eg 6 different colors, must of course be at least as long as the number of objects you want to use this color with
ndc = new_colors(np.linspace(0,1,N)) # make them discrete, ndc = new discrete colors

#boxplotting all
fig, ax = plt.subplots(1,2, figsize=(8,4))
fig.tight_layout(pad=2.5)

sns.boxplot(x='cpd', y='err_rate', hue='delay', data=error_rate, ax=ax[0], palette = ndc)
ax[0].set_ylabel('error rate [%]')
ax[0].get_legend().remove()
ax[0].spines['top'].set_visible(False)
ax[0].spines['right'].set_visible(False)
#ax[0].spines['bottom'].set_linewidth(2.0)
#ax[0].spines['left'].set_linewidth(2.0)
#ax[0].xaxis.set_tick_params(width=2)
#ax[0].yaxis.set_tick_params(width=2)
fig.legend(title='Delay [s]', ncols=3, loc='upper center')

sns.boxplot(x='cpd', y='mean', hue='delay', data=resp_time, ax=ax[1], palette = ndc)
ax[1].set_ylabel('response time [s]')
ax[1].get_legend().remove()
ax[1].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
#ax[1].spines['bottom'].set_linewidth(2.0)
#ax[1].spines['left'].set_linewidth(2.0)
#ax[1].xaxis.set_tick_params(width=2)
#ax[1].yaxis.set_tick_params(width=2)
plt.show()

#-----------------------------------------------------------------------------------

fig, ax = plt.subplots(1,2, figsize=(8,4))
fig.tight_layout(pad=2.5)
sns.boxplot(x='cpd', y='mean', hue='delay', data=shifts, ax=ax[0], palette = ndc)
ax[0].get_legend().remove()
ax[0].set_ylabel('number of switches')
ax[0].spines['top'].set_visible(False)
ax[0].spines['right'].set_visible(False)
#ax[0].spines['bottom'].set_linewidth(2.0)
#ax[0].spines['left'].set_linewidth(2.0)
#ax[0].xaxis.set_tick_params(width=2)
#ax[0].yaxis.set_tick_params(width=2)
fig.legend(title='Delay [s]', ncols=3, loc='upper center')

sns.boxplot(x='cpd', y='mean', hue='delay', data=proc_time, ax=ax[1], palette = ndc)
ax[1].set_ylabel('processing time [s]')
ax[1].get_legend().remove()
ax[1].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
#ax[1].spines['bottom'].set_linewidth(2.0)
#ax[1].spines['left'].set_linewidth(2.0)
#ax[1].xaxis.set_tick_params(width=2)
#ax[1].yaxis.set_tick_params(width=2)

plt.show()
