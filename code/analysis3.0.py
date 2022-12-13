from typing import Dict, Union, List, Any

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython import embed

df = pd.read_csv('../data_processed/cvs.csv', delimiter=';', header=0)
cpds = [2,8]
delay = [0,2]
names = ['eva','Lorenz','Patrick', 'Sofie', 'VP2', 'vp4', 'VP5', 'vp6', 'VP7']

print(df)

#response time

#create dictionary with references to cpds and delay list (so it's soft-coded) and empty list to fill in values
resp_time = dict({"cpds": [cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1]], "delay": [delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1]], "mean": [], "subj": []})

for i in cpds:
    print(i)
    #print(df['cpd'])
    subdf = df[df.cpd == i]

    for name in names:
        subsubdf = subdf[subdf.subj == name]

        respt_mean = np.array(subsubdf.totdur.groupby(df.delay).mean())
        resp_time["mean"].append(respt_mean[0])
        resp_time["subj"].append(name)
        resp_time["mean"].append(respt_mean[1])
        resp_time["subj"].append(name)

print('response time')
print(resp_time)

resp_time_result = pd.DataFrame(resp_time)

resp_time_result.to_csv('resp_time.csv')

""""
#response time old (mean over all values)

resp_time = dict({"cpds": [2,2,8,8], "delay": [0,2,0,2], "median": []})
print(resp_time)

for i in cpds:
    subdf = df[df.cpd == i]

    resp_time_median = np.array(subdf.totdur.groupby(df.delay).median())
    print(resp_time_median)
    resp_time["median"].append(resp_time_median[0])
    resp_time["median"].append(resp_time_median[1])

print(resp_time)
"""
#shifts

shifts = dict({"cpds": [cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1]], "delay": [delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1]], "mean": [], "subj": []})

for i in cpds:
    subdf = df[df.cpd == i]

    #shift_means = np.ones([2, len(names)])
    #shift_means_2 = np.ones(len(names))
    for name in names:
        subsubdf = subdf[subdf.subj == name]

        shifts_mean = np.array(subsubdf.switches.groupby(df.delay).mean())
        shifts["mean"].append(shifts_mean[0])
        shifts["subj"].append(name)
        shifts["mean"].append(shifts_mean[1])
        shifts["subj"].append(name)
print('shifts')
print(shifts)

shift_result = pd.DataFrame(shifts)

shift_result.to_csv('shifts.csv')

#processing time

proc_time = dict({"cpds": [cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1]], "delay": [delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1]], "mean": [], "subj": []})

for i in cpds:
    subdf = df[df.cpd == i]

    #proct_means = np.ones([2, len(names)])

    for name in names:
        subsubdf = subdf[subdf.subj == name]

        proct_mean = np.array(subsubdf.tpertrial.groupby(df.delay).mean())
        proc_time["mean"].append(proct_mean[0])
        proc_time["subj"].append(name)
        proc_time["mean"].append(proct_mean[1])
        proc_time["subj"].append(name)
print('processing time')
print(proc_time)

proc_time_result = pd.DataFrame(proc_time)

proc_time_result.to_csv('proc_time.csv')

#error rate

error_rate = dict({"cpds": [cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[0],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1],cpds[1]], "delay": [delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1],delay[0],delay[1]], "err_rate": [], "subj": []})

for i in cpds:
    subdf = df[df.cpd == i]

    error_rates = np.ones([2, len(names)])

    for name in names:
        subsubdf = subdf[subdf.subj == name]

        err_rate = (np.array(subsubdf.iserror.groupby(df.delay).sum()) / 15) * 100

        error_rate["err_rate"].append(err_rate[0])
        error_rate["subj"].append(name)
        error_rate["err_rate"].append(err_rate[1])
        error_rate["subj"].append(name)

print('error_rate')
print(error_rate)

error_rate_result = pd.DataFrame(error_rate)

error_rate_result.to_csv('error_rate.csv')