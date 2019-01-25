import numpy as np
import pandas as pd
from scipy.special import expit as logit

tau = 2*np.pi
np.random.seed(3141597)
# def lumi(x):
#     a = 2.
#     b = 1.
#     r = 1.
#
#     x = (x%tau)/tau*2*a - a
#
#     y = b*(1 - (np.abs(x)/a)**(2*a/r))**(r/2/b)
#     return y
def lumi(x):
    x = (x%tau)
    up = 6./24.*tau
    down = 18./24.*tau
    width = 1/24.*tau
    return logit((x - up)/width) - logit((x - down)/width)

# constants
sigma_T = 0.5
sigma_L = 1

# temperature constant
T = np.random.normal(23.2, sigma_T, 1000)
np.save("data/temperature_constant.npy", T)

# temperature/luminosity timeseries
# points per hour
n = 10
# days
d = 3
N = 24*n*d

# time
t = np.linspace(0, tau*d, N, endpoint=False)
# temperature
t_in_hours = t/tau*24
T = (-np.cos(t) + 1)*0.5*20 + np.random.normal(0, sigma_T ,N) + 5
L = lumi(t)*50 + np.random.normal(0, sigma_L, N) + 10

# data = np.vstack((t_in_hours, T, L)).T
# df = pd.DataFrame(data=data, columns=["hours", "temperature", "luminosity"])
df = pd.DataFrame({"hours": t_in_hours, "temperature": T, "luminosity": L})
df = df.set_index("hours")
df.to_csv("data/temperature_day.csv")
