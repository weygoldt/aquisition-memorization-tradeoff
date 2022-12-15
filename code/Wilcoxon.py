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
resp_time_cpds = dict({"cpd": [2,2,2,2,2,2,2,2,2,8,8,8,8,8,8,8,8,8], "mean": [], "subj": []})

for i in cpds:
    subdf = resp_time[resp_time.cpd == i]

    # Wilcoxon signed rank
    delay0 = subdf[subdf['delay'] == 0]
    delay2 = subdf[subdf['delay'] == 2]
    stats = wilcoxon(delay0['mean'], delay2['mean'])
    print(f'resp_time, delay {i}cpd')
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
cpds2 = resp_time[resp_time['cpd'] == 2]
cpds8 = resp_time[resp_time['cpd'] == 8]

stats = wilcoxon(cpds2['mean'], cpds8['mean'])
print('resp_time, cpd')
print(stats)

#--------------------------------------------------------------------------------------------
shifts_cpds = dict({"cpd": [2,2,2,2,2,2,2,2,2,8,8,8,8,8,8,8,8,8], "mean": [], "subj": []})

for i in cpds:
    subdf = shifts[shifts.cpd == i]

    # Wilcoxon signed rank
    delay0 = subdf[subdf['delay'] == 0]
    delay2 = subdf[subdf['delay'] == 2]
    stats = wilcoxon(delay0['mean'], delay2['mean'])
    print(f'shifts, delay {i}cpd')
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
cpds2 = shifts[shifts['cpd'] == 2]
cpds8 = shifts[shifts['cpd'] == 8]

stats = wilcoxon(cpds2['mean'], cpds8['mean'])
print('shifts, cpd')
print(stats)

#--------------------------------------------------------------------------------------------
proc_time_cpds = dict({"cpd": [2,2,2,2,2,2,2,2,2,8,8,8,8,8,8,8,8,8], "mean": [], "subj": []})

for i in cpds:
    subdf = proc_time[proc_time.cpd == i]

    # Wilcoxon signed rank
    delay0 = subdf[subdf['delay'] == 0]
    delay2 = subdf[subdf['delay'] == 2]
    stats = wilcoxon(delay0['mean'], delay2['mean'])
    print(f'proc_time, delay {i}cpd')
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
cpds2 = proc_time[proc_time['cpd'] == 2]
cpds8 = proc_time[proc_time['cpd'] == 8]

stats = wilcoxon(cpds2['mean'], cpds8['mean'])
print('proc_time, cpd')
print(stats)

#mean per person
proc_time_mean = dict({"mean": [], "std": [], "subj": []})

for name in names:
    subdf = proc_time[proc_time.subj == name]

    mean = np.mean(subdf['mean'])
    std = np.std(subdf['mean'])
    # print(mean)
    proc_time_mean['mean'].append(mean)
    proc_time_mean['std'].append(std)
    proc_time_mean['subj'].append(name)

proc_time_means = pd.DataFrame(proc_time_mean)
#proc_time_means.to_csv('proc_time_means.csv')

#--------------------------------------------------------------------------------------------
error_rate_cpds = dict({"cpd": [2,2,2,2,2,2,2,2,2,8,8,8,8,8,8,8,8,8], "err_rate": [], "subj": []})

for i in cpds:
    subdf = error_rate[error_rate.cpd == i]

    # Wilcoxon signed rank
    delay0 = subdf[subdf['delay'] == 0]
    delay2 = subdf[subdf['delay'] == 2]
    stats = wilcoxon(delay0['err_rate'], delay2['err_rate'])
    print(f'error_rate, delay {i}cpd')
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
cpds2 = error_rate[error_rate['cpd'] == 2]
cpds8 = error_rate[error_rate['cpd'] == 8]

stats = wilcoxon(cpds2['err_rate'], cpds8['err_rate'])
print('error_rate, cpd')
print(stats)

###linear regression

print(proc_time_means)
t = [0.0635, 0.083, 0.062, 0.041, 0.039, 0.066]
threshs = dict({"thresh": t, "proc_time": [4.166210317,
3.171673667,
2.509800377,
1.273602472,
3.568377639,
1.72297342], "subj": ['Lorenz', 'Patrick', 'VP5', 'VP7', 'eva', 'vp4']})
threshs = pd.DataFrame(threshs)


def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="b", marker="o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1] * x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('mean detection threshold')
    plt.ylabel('processing time')

    # function to show plot
    plt.show()


"""def main():
    # observations / data
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))

    # plotting regression line
    plot_regression_line(x, y, b)"""

print(threshs)

x = threshs['thresh']
y= threshs['proc_time']
b = estimate_coef(x,y)
print(b)

plot_regression_line(x,y,b)