import numpy as np
from scipy.stats import norm

# define variables
r = 2.148
S = 163.98
K = 105
T = 30 / 365
sigma = 0.3352


def blackScholes(r, S, K, T, sigma, type="C"):
    # "Calculate BlackSholes option price for a call/put"
    d1 = (np.log(S / K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    try:
        if type == "C":
            price = S * norm.cdf(d1, 0, 1) - K * np.exp(-r * T) * norm.cdf(d2, 0, 1)
        elif type == "P":
            price = K * np.exp(-r * T) * norm.cdf(-d2, 0, 1) - S * norm.cdf(-d1, 0, 1)
        return price
    except:
        print("Please confirm all option parameters above!!!")


print("Option Price is: ", round(blackScholes(r, S, K, T, sigma, type="C"), 2))
