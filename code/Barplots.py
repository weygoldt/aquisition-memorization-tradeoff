import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#from analysis2.0 import resp_time, shifts, proc_time, error_rate

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

print(shifts)

sns.catplot(x='cpds', y='median', hue='delay', data=resp_time, kind='bar')
#plt.show()

sns.catplot(x='cpds', y='median', hue='delay', data=shifts, kind='bar')
#plt.show()

sns.catplot(x='cpds', y='median', hue='delay', data=proc_time, kind='bar')
#plt.show()

sns.catplot(x='cpds', y='median', hue='delay', data=error_rate, kind='bar', )
plt.show()