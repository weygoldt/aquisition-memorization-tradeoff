from scipy.stats import wilcoxon
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import cmocean

#from analysis3.0 import resp_time, shifts, proc_time, error_rate

error_rate = pd.read_csv('error_rate.csv', header=0)
#error_rate.drop(["NaN"], inplace=True)
resp_time = pd.read_csv('resp_time.csv', header=0)
#resp_time.drop(["NaN"], inplace=True)
proc_time = pd.read_csv('proc_time.csv', header=0)
#proc_time.drop(["NaN"], inplace=True)
shifts = pd.read_csv('shifts.csv', header=0)
#shifts.drop(["NaN"], inplace=True)

#print(shifts)
cpds = [2,8]
names = ['eva','Lorenz','Patrick', 'Sofie', 'VP2', 'vp4', 'VP5', 'vp6', 'VP7']

shifts_cpds = dict({"cpds": [2,2,2,2,2,2,2,2,2,8,8,8,8,8,8,8,8,8], "mean": [], "subj": []})

for i in cpds:
    subdf = shifts[shifts.cpds == i]

    # Wilcoxon signed rank
    delay0 = subdf[subdf['delay'] == 0]
    delay2 = subdf[subdf['delay'] == 2]
    stats = wilcoxon(delay0['mean'], delay2['mean'])
    print(f'shifts, delay {i}cpds')
    print(stats)

    for name in names:
        subsubdf = subdf[subdf.subj == name]

        mean = np.mean(subsubdf['mean'])
        #print(mean)
        shifts_cpds['mean'].append(mean)
        shifts_cpds['subj'].append(name)

print(shifts_cpds)

shifts = pd.DataFrame(shifts_cpds)
#shifts.to_csv('shifts_cpds.csv')

#Wilcoxon signed rank
cpds2 = shifts[shifts['cpds'] == 2]
cpds8 = shifts[shifts['cpds'] == 8]

stats = wilcoxon(cpds2['mean'], cpds8['mean'])
print('shifts, cpds')
print(stats)