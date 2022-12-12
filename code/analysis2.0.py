import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython import embed

df = pd.read_csv('../data_processed/cvs.csv')

resp_time = dict({"cpds": [2,2,8,8], "delay": [0,2,0,2], "median": []})
print(resp_time)

cpds = [2,8]

for i in cpds:
    subdf = df[df.cpd == i]

    resp_time_median = np.array(subdf.totdur.groupby(df.delay).median())
    print(resp_time_median)
    resp_time["median"].append(resp_time_median[0],d.resp_time_median[1]