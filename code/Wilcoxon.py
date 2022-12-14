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

#-----------------------------------------------------------------------------------------------
resp_time_cpds = dict({"cpds": [2,2,2,2,2,2,2,2,2,8,8,8,8,8,8,8,8,8], "mean": [], "subj": []})

for i in cpds:
    subdf = resp_time[resp_time.cpds == i]

    # Wilcoxon signed rank
    delay0 = subdf[subdf['delay'] == 0]
    delay2 = subdf[subdf['delay'] == 2]
    stats = wilcoxon(delay0['mean'], delay2['mean'])
    print(f'resp_time, delay {i}cpds')
    print(stats)

    #mean of 0s and 2s delay values per person
    for name in names:
        subsubdf = subdf[subdf.subj == name]

        mean = np.mean(subsubdf['mean'])
        #print(mean)
        resp_time_cpds['mean'].append(mean)
        resp_time_cpds['subj'].append(name)

#print(resp_time_cpds)

resp_time = pd.DataFrame(resp_time_cpds)
#resp_time.to_resp_timecsv('resp_time_cpds.csv')

#Wilcoxon signed rank
cpds2 = resp_time[resp_time['cpds'] == 2]
cpds8 = resp_time[resp_time['cpds'] == 8]

stats = wilcoxon(cpds2['mean'], cpds8['mean'])
print('resp_time, cpds')
print(stats)

#--------------------------------------------------------------------------------------------
shifts_cpds = dict({"cpds": [2,2,2,2,2,2,2,2,2,8,8,8,8,8,8,8,8,8], "mean": [], "subj": []})

for i in cpds:
    subdf = shifts[shifts.cpds == i]

    # Wilcoxon signed rank
    delay0 = subdf[subdf['delay'] == 0]
    delay2 = subdf[subdf['delay'] == 2]
    stats = wilcoxon(delay0['mean'], delay2['mean'])
    print(f'shifts, delay {i}cpds')
    print(stats)

    #mean of 0s and 2s delay values per person
    for name in names:
        subsubdf = subdf[subdf.subj == name]

        mean = np.mean(subsubdf['mean'])
        #print(mean)
        shifts_cpds['mean'].append(mean)
        shifts_cpds['subj'].append(name)

#print(shifts_cpds)

shifts = pd.DataFrame(shifts_cpds)
#shifts.to_csv('shifts_cpds.csv')

#Wilcoxon signed rank
cpds2 = shifts[shifts['cpds'] == 2]
cpds8 = shifts[shifts['cpds'] == 8]

stats = wilcoxon(cpds2['mean'], cpds8['mean'])
print('shifts, cpds')
print(stats)

#--------------------------------------------------------------------------------------------
proc_time_cpds = dict({"cpds": [2,2,2,2,2,2,2,2,2,8,8,8,8,8,8,8,8,8], "mean": [], "subj": []})

for i in cpds:
    subdf = proc_time[proc_time.cpds == i]

    # Wilcoxon signed rank
    delay0 = subdf[subdf['delay'] == 0]
    delay2 = subdf[subdf['delay'] == 2]
    stats = wilcoxon(delay0['mean'], delay2['mean'])
    print(f'proc_time, delay {i}cpds')
    print(stats)

    #mean of 0s and 2s delay values per person
    for name in names:
        subsubdf = subdf[subdf.subj == name]

        mean = np.mean(subsubdf['mean'])
        #print(mean)
        proc_time_cpds['mean'].append(mean)
        proc_time_cpds['subj'].append(name)

#print(proc_time_cpds)

proc_time = pd.DataFrame(proc_time_cpds)
#proc_time.to_csv('proc_time_cpds.csv')

#Wilcoxon signed rank
cpds2 = proc_time[proc_time['cpds'] == 2]
cpds8 = proc_time[proc_time['cpds'] == 8]

stats = wilcoxon(cpds2['mean'], cpds8['mean'])
print('proc_time, cpds')
print(stats)

#--------------------------------------------------------------------------------------------
error_rate_cpds = dict({"cpds": [2,2,2,2,2,2,2,2,2,8,8,8,8,8,8,8,8,8], "err_rate": [], "subj": []})

for i in cpds:
    subdf = error_rate[error_rate.cpds == i]

    # Wilcoxon signed rank
    delay0 = subdf[subdf['delay'] == 0]
    delay2 = subdf[subdf['delay'] == 2]
    stats = wilcoxon(delay0['err_rate'], delay2['err_rate'])
    print(f'error_rate, delay {i}cpds')
    print(stats)

    #mean of 0s and 2s delay values per person
    for name in names:
        subsubdf = subdf[subdf.subj == name]

        mean = np.mean(subsubdf['err_rate'])
        #print(mean)
        error_rate_cpds['err_rate'].append(mean)
        error_rate_cpds['subj'].append(name)

#print(error_rate_cpds)

error_rate = pd.DataFrame(error_rate_cpds)
#error_rate.to_csv('error_rate_cpds.csv')

#Wilcoxon signed rank
cpds2 = error_rate[error_rate['cpds'] == 2]
cpds8 = error_rate[error_rate['cpds'] == 8]

stats = wilcoxon(cpds2['err_rate'], cpds8['err_rate'])
print('error_rate, cpds')
print(stats)