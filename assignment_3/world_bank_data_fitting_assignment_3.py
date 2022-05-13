# IMPORTANT LIBRARIES
import wbgapi as wb
import scipy.optimize as opt
import numpy as np
import itertools as iter
import matplotlib.pyplot as plt

"""
FUNCTION THAT COMPUTES EXPONENTIAL FUNCTION
"""


def exp_growth(t, scale, growth):
    f = scale * np.exp(growth * (t-1950))
    return f


"""
FUNCTION THAT COMPUTES LOGISTICS FUNCTION
"""


def logistics(t, scale, growth, t0):

    f = scale / (1.0 + np.exp(-growth * (t - t0)))
    return f


"""
CALCULATES THE UPPER AND LOWER LIMITS FOR THE FUNCTION, PARAMETERS AND
SIGMAS FOR SINGLE VALUE OR ARRAY X. FUNCTIONS VALUES ARE CALCULATED FOR
ALL COMBINATIONS OF +/- SIGMA AND THE MINIMUM AND MAXIMUM IS DETERMINED
CAN BE USED FOR ALL NUMBER OF PARAMETERS AND SIGMAS >=1
"""


def err_ranges(x, func, param, sigma):

    lower = func(x, *param)
    upper = lower

    uplow = []

    for p, s in zip(param, sigma):
        pmin = p - s
        pmax = p + s
        uplow.append((pmin, pmax))

    pmix = list(iter.product(*uplow))

    for p in pmix:
        y = func(x, *p)
        lower = np.minimum(lower, y)
        upper = np.maximum(upper, y)

    return lower, upper


# COUNTRY CODES WITH THEIR RESPECTIVE COUNTRY NAMES
country_names = {"PAK": "Pakistan"}

# DEFINING IMPORTANT INDICATORS
total_population = "SP.POP.TOTL"

# DEFINING DATAFRAME WITH COUNTRY DATA THAT MATCH THE INDICATORS
dataframe1 = wb.data.DataFrame([total_population],
                               country_names,
                               time=range(1961, 2021),
                               numericTimeKeys=True,
                               columns='series').reset_index()

# GIVE COLUMNS APPROPRIATE NAMES
dataframe1.rename(columns={'economy': 'Country',
                           'time': 'Year',
                           'SP.POP.TOTL': 'Population'},
                  inplace=True)

# DEFINING DATAFRAME WITH COUNTRY DATA THAT MATCH THE INDICATORS
# THIS IS TO COMPARE POPULATIONS OF BOTH DATAFRAMES
dataframe2 = wb.data.DataFrame([total_population],
                               country_names,
                               time=range(1960, 2020),
                               numericTimeKeys=True,
                               columns='series').reset_index()

# GIVE COLUMNS APPROPRIATE NAMES
dataframe2.rename(columns={'economy': 'Country',
                           'time': 'Year',
                           'SP.POP.TOTL': 'Population'},
                  inplace=True)

# DROP Year COLUMN
dataframe2.drop(['Year'], inplace=True, axis=1)

# CALCULATE THE INCREASE IN POPULATION AND SAVE IT TO THE DATAFRAME
dataframe1['Population Increase'] = dataframe1[
    'Population'] / dataframe2['Population']

# FIT EXPONENTIAL GROWTH
popt, covar = opt.curve_fit(exp_growth,
                            dataframe1["Year"],
                            dataframe1["Population"])

dataframe1["pop_exp"] = exp_growth(dataframe1["Year"], *popt)

plt.figure()
plt.plot(dataframe1["Year"], dataframe1["Population"], label="data")
plt.plot(dataframe1["Year"], dataframe1["pop_exp"], label="fit")

plt.legend()
plt.title("First fit attempt")
plt.xlabel("year")
plt.ylabel("population")
plt.show()
print()

popt = [4e8, 0.01]
dataframe1["pop_exp"] = exp_growth(dataframe1["Year"], *popt)

plt.figure()
plt.plot(dataframe1["Year"], dataframe1["Population"], label="data")
plt.plot(dataframe1["Year"], dataframe1["pop_exp"], label="fit")

plt.legend()
plt.xlabel("year")
plt.ylabel("population")
plt.title("Improved start value")
plt.show()

# FIT EXPONENTIAL GROWTH
popt, covar = opt.curve_fit(exp_growth,
                            dataframe1["Year"],
                            dataframe1["Population"], p0=[4e8, 0.02])

dataframe1["pop_exp"] = exp_growth(dataframe1["Year"], *popt)

plt.figure()
plt.plot(dataframe1["Year"], dataframe1["Population"], label="data")
plt.plot(dataframe1["Year"], dataframe1["pop_exp"], label="fit")

plt.legend()
plt.xlabel("year")
plt.ylabel("population")
plt.title("Final fit exponential growth")
plt.show()

popt = [8e8, 0.02, 1990]
dataframe1["pop_log"] = logistics(dataframe1["Year"], *popt)

plt.figure()
plt.plot(dataframe1["Year"], dataframe1["Population"], label="data")
plt.plot(dataframe1["Year"], dataframe1["pop_log"], label="fit")

plt.legend()
plt.xlabel("year")
plt.ylabel("population")
plt.title("Improved start value")
plt.show()

popt, covar = opt.curve_fit(logistics,
                            dataframe1["Year"],
                            dataframe1["Population"],
                            p0=(2e9, 0.05, 1990.0))

dataframe1["pop_log"] = logistics(dataframe1["Year"], *popt)

plt.figure()
plt.title("logistics function")
plt.plot(dataframe1["Year"], dataframe1["Population"], label="data")
plt.plot(dataframe1["Year"], dataframe1["pop_log"], label="fit")

plt.legend()
plt.xlabel("year")
plt.ylabel("population")
plt.show()

sigma = np.sqrt(np.diag(covar))

low, up = err_ranges(dataframe1["Year"], logistics, popt, sigma)

plt.figure()
plt.title("logistics function")
plt.plot(dataframe1["Year"], dataframe1["Population"], label="data")
plt.plot(dataframe1["Year"], dataframe1["pop_log"], label="fit")

plt.fill_between(dataframe1["Year"], low, up, alpha=0.7)
plt.legend()
plt.xlabel("year")
plt.ylabel("population")
plt.show()

print("Forcasted population")
low, up = err_ranges(2030, logistics, popt, sigma)
print("2030 between", low, "and", up)
low, up = err_ranges(2040, logistics, popt, sigma)
print("2040 between", low, "and", up)
low, up = err_ranges(2050, logistics, popt, sigma)
print("2050 between", low, "and", up)

print("Forcasted population")
low, up = err_ranges(2030, logistics, popt, sigma)
mean = (up + low) / 2.0
pm = (up - low) / 2.0
print("2030:", mean, "+/-", pm)

low, up = err_ranges(2040, logistics, popt, sigma)
mean = (up + low) / 2.0
pm = (up - low) / 2.0
print("2040:", mean, "+/-", pm)

low, up = err_ranges(2050, logistics, popt, sigma)
mean = (up + low) / 2.0
pm = (up - low) / 2.0
print("2050:", mean, "+/-", pm)
