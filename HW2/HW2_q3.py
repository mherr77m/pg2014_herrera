# !env Python
# Michael Herrera
# 10/18/14
# HW2, Problem 3
# Passes the function the data to a high pass filter
# that removes the trend with a given order polynomial.

import numpy as np
import matplotlib.pyplot as plt

def high_pass(x, y, n = 1):
    """
    High pass filter.  Takes x,y data as input and removes
    the trend from the data based on a polynomial function
    of the given order, default is linear.
    """
    psol = np.polynomial.Polynomial.fit(x, y, n)
    new_y = psol(x)
    return y - new_y

if __name__ == '__main__':
    num = 1000
    x = 6 * np.random.rand(num) - 3
    y = x**4 - 4 * x**2 + x + 2.5 * np.random.randn(num)

    y_filtered = high_pass(x, y, 4)

    fig = plt.figure(figsize=(8,7))
    ax = fig.add_subplot(111)
    ax.plot(x, y_filtered, 'bx', label = 'Filtered Data')
    ax.plot(x, y, 'k.', label = 'Raw Data')
    plt.title('High Pass Filter')
    plt.legend(loc = 2)
    plt.savefig('High_Pass_Filter.pdf')

    print "\nPlot for problem 3 has been saved as High_Pass_Filter.pdf\n"





