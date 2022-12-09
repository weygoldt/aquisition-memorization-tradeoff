import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython import embed

df = pd.read_csv('../data_processed/cvs.csv')

cpds = [2,8]
for i in cpds:

    subdf = df[df.cpd == i]

    resp_time_mean = np.array(subdf.totdur.groupby(df.delay).mean())
    resp_time_std = np.array(subdf.totdur.groupby(df.delay).std())
    shifts_mean = np.array(subdf.switches.groupby(df.delay).mean())
    shifts_std = np.array(subdf.switches.groupby(df.delay).std())
    proc_time_mean = np.array(subdf.tpertrial.groupby(df.delay).mean())
    proc_time_std = np.array(subdf.tpertrial.groupby(df.delay).std())

    #print(subdf)
    # error rate (müsste dann eigentlich der median sein, wenn wir so wenige subjects haben)

    error_rates = []
    #Problem: Wenn wir einfach name in subdf.subj schreiben kriegen wir 30 Ergebnisse pro VP
    for name in ['eva','Lorenz','Patrick']:
        subsubdf = subdf[subdf.subj == name]
        error_rate = (np.array(subsubdf.iserror.groupby(df.delay).sum()) / 15) * 100
        error_rates.append(error_rate)
        print(error_rate)
        #print(error_rates)
        #embed()
    #error_rates = np.array(error_rates)
    error_rate_median_0 = np.median(error_rates[0])
    error_rate_median_2 = np.median(error_rates[1])
    print(error_rates)
    print(error_rate_median_0)
    print(error_rate_median_2)
