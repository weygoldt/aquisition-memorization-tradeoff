import matplotlib.pyplot as plt
import numpy as np


def figsave(path: str) -> None:
    plt.savefig(f"{path}.svg")
    plt.savefig(f"{path}.pdf")

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
