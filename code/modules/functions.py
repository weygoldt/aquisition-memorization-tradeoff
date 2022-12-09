import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#test

def exec_timer(function):
    """
    exec_timer is a decorator function to print the execution time of another function.

    Parameters
    ----------
    function : function
        The function which execution should be timed.

    Returns
    -------
    *args **kwargs
        What the input function returned. 
    """
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(function.__name__, t2))
        return result

    return wrapper


@exec_timer
def bound_logistic(lowerb=None, upperb=None):
    """
    Returns a logistic function within the specified upper and lower bounds.
    Particularly useful for fitting psychometric curves with unconventional 
    chance levels (i.e. 0.25 for a 4AFC test).

    Returns
    -------
    function
        The logistic
    """

    lowerb = 0 if lowerb is None else lowerb
    upperb = 1 if upperb is None else upperb

    def logistic(x, x0, k):
        """
        logistic returns a standard logistic function constrained to two min and max values (e.g. for fitting).

        Parameters
        ----------
        x : array-like
            The x data (e.g. time, stimulus levels, ...)
        x0 : float
            The x value of the sigmoids midpoint
        k : float
            The logistic growth rate or steepness of the curve

        Returns
        -------
        array-like
            The y values for the logistic function.
        """
        return lowerb + (upperb-lowerb)*(1/(1 + np.exp(-k*(x-x0))))

    return logistic

#analyse für graphiken
cpds = [2,8]
def analysis(df, cpds)

    for i in cpds:
        subdf = df[df.cpd == i]
        resp_time_mean = np.array(subdf.tordur.groupby(df.delay).mean())
        resp_time_std = np.array(subdf.tordur.groupby(df.delay).std())
        shifts_mean = np.array(subdf.switches.groupby(df.delay).mean())
        shifts_std = np.array(subdf.switches.groupby(df.delay).std())
        proc_time_mean = np.array(subdf.tpertrial.groupby(df.delay).mean())
        proc_time_std = np.array(subdf.tpertrial.groupby(df.delay).std())

        # error rate (müsste dann eigentlich der median sein, wenn wir so wenige subjects haben)
        error_rates = np.array()
        for k in [1:(len(df.subj)/60+1)]
            subsubdf = subdf[subdf.subj == VPk]
            error_rate = np.array(subsubdf.error.groupby(df.delay).sum()) / 15
            error_rates.append(error_rate)

        error_rate_median = np.median(error_rates)

    #hier arrays an analyse-dataframe anfügen



    return (analyse-dataframe)

#es fehlt: anständiger loop für error rate (wie durch subj iterieren?)
#          sinnvoller return -> ein dataframe mit 2 dimensionen (2 & 8 cpds), der dann darin die jeweils 4 arrays aus dem loop vorhält