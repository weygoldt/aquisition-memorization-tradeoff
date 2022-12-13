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

print(shifts)
cpds = [2,8]
names = ['eva','Lorenz','Patrick', 'Sofie', 'VP2', 'vp4', 'VP5', 'vp6', 'VP7']

shifts_cpds = dict({"cpds": [2,2,2,2,2,8,8,8,8,8], "mean": [], "subj": []})

for i in cpds:
    subdf = shifts[shifts.cpds == i]

    for name in names:
        subsubdf = subdf[subdf.subj == name]

        mean = np.array(subsubdf['mean'].mean())
        shifts["mean"].append(mean)
        shifts["subj"].append(name)
        print(name)
        print(mean)
print(shifts_cpds)
