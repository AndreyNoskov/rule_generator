import matplotlib.pyplot as plt
import numpy as np
from numpy import polyval


def plot_time_per_rule(times):
    x = range(1, len(times)+1)
    # print(x)
    # app = np.polyfit(np.array(x), np.array(times), 2)
    # print(app)
    # approx_vals = np.polyval(np.array(x), app)
    # print(approx_vals)
    plt.plot(x, times, 'k')
    plt.ylabel('Time per rule')
    plt.xlabel('Rule number')
    plt.show()
