from typing import Dict, Union, List, Any

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython import embed

df = pd.read_csv('../data_processed/cvs.csv')
cpds = [2,8]
names = ['eva','Lorenz','Patrick', 'VP2', 'VP5']

#response_time

resp_time = dict({"cpds": [2,2,8,8], "delay": [0,2,0,2], "median": []})

for i in cpds:
    subdf = df[df.cpd == i]

    respt_means = np.ones([2, len(names)])

    for k,name in enumerate(names):
        subsubdf = subdf[subdf.subj == name]

        respt_mean = np.array(subdf.totdur.groupby(df.delay).mean())
        respt_means[0, k] = respt_mean[0]
        respt_means[1, k] = respt_mean[1]

    respt_median = np.median(respt_means, 1)
    resp_time["median"].append(respt_median[0])
    resp_time["median"].append(respt_median[1])
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

shifts = dict({"cpds": [2,2,8,8], "delay": [0,2,0,2], "median": []})

for i in cpds:
    subdf = df[df.cpd == i]

    shift_means = np.ones([2, len(names)])
    #shift_means_2 = np.ones(len(names))
    for k,name in enumerate(names):
        subsubdf = subdf[subdf.subj == name]

        shifts_mean = np.array(subdf.switches.groupby(df.delay).mean())
        shift_means[0, k] = shifts_mean[0]
        shift_means[1, k] = shifts_mean[1]

    #print('shift_means')
    #print(shift_means)
    shifts_median = np.median(shift_means, 1)
    shifts["median"].append(shifts_median[0])
    shifts["median"].append(shifts_median[1])
print('shifts')
print(shifts)

shift_result = pd.DataFrame(shifts)

shift_result.to_csv('shifts.csv')

#processing time

proc_time = dict({"cpds": [2, 2, 8, 8], "delay": [0, 2, 0, 2], "median": []})

for i in cpds:
    subdf = df[df.cpd == i]

    proct_means = np.ones([2, len(names)])

    for k, name in enumerate(names):
        subsubdf = subdf[subdf.subj == name]

        proct_mean = np.array(subdf.tpertrial.groupby(df.delay).mean())
        proct_means[0, k] = proct_mean[0]
        proct_means[1, k] = proct_mean[1]

    proct_median = np.median(proct_means, 1)
    proc_time["median"].append(proct_median[0])
    proc_time["median"].append(proct_median[1])
print('processing time')
print(proc_time)

proc_time_result = pd.DataFrame(proc_time)

proc_time_result.to_csv('proc_time.csv')

#error rate

error_rate = dict({"cpds": [2, 2, 8, 8], "delay": [0, 2, 0, 2], "median": []})

for i in cpds:
    subdf = df[df.cpd == i]

    error_rates = np.ones([2, len(names)])

    for k, name in enumerate(names):
        subsubdf = subdf[subdf.subj == name]

        err_rate = (np.array(subsubdf.iserror.groupby(df.delay).sum()) / 15) * 100

        error_rates[0, k] = err_rate[0]
        error_rates[1, k] = err_rate[1]
        #print('error_rates')
        #print(error_rates)

    error_rate_median = np.median(error_rates, 1)
    #print('error_rate_median')
    #print(error_rate_median)
    error_rate["median"].append(error_rate_median[0])
    error_rate["median"].append(error_rate_median[1])

print('error_rate')
print(error_rate)

error_rate_result = pd.DataFrame(error_rate)

error_rate_result.to_csv('error_rate.csv')