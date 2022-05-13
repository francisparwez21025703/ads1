# IMPORTANT LIBRARIES
import numpy as np
import wbgapi as wb
import sklearn.cluster as cluster
import matplotlib.pyplot as plt


"""
FUNCTION TO NORMALISE ARRAY TO [0, 1]
"""


def norm(array):

    min_val = np.min(array)
    max_val = np.max(array)

    scaled = (array-min_val) / (max_val-min_val)

    return scaled


"""
FUNCTION TO NORMALISE DATAFRAME TO [0, 1]
"""


def norm_df(df):

    for col in df.columns[1:]:
        df[col] = norm(df[col])

    return df


"""
FUNCTION TO CREATE SQUARE PLOT OF THE FIRST TWO COLUMNS OF DATAFRAME
USING A SMALL CIRCLE
"""


def makeplot(df, col1, col2):

    plt.figure(figsize=(5.0, 5.0))
    plt.plot(df[col1], df[col2], "o", markersize=3)

    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()


"""
CREATING A NEW DATAFRAME WITH DATA FROM THE WORLD BANK API
BASED ON GIVEN INDICATORS
"""

# COUNTRY CODES WITH THEIR RESPECTIVE COUNTRY NAMES
country_names = {"GBR": "United Kingdom",
                 "USA": "United States",
                 "PAK": "Pakistan",
                 "CAN": "Canada",
                 "ITA": "Italy",
                 "AUS": "Australia",
                 "BRA": "Brazil",
                 "CHN": "China",
                 "CRI": "Costa Rica",
                 "DNK": "Denmark",
                 "SLV": "El Salvador"}

# DEFINING IMPORTANT INDICATORS
co2_indicator = "EN.ATM.CO2E.KT"
co2_from_manufacturers = "EN.CO2.MANF.ZS"

# DEFINING DATAFRAME WITH COUNTRY DATA THAT MATCH THE INDICATORS
dataframe = wb.data.DataFrame([co2_indicator,
                               co2_from_manufacturers],
                              country_names,
                              time=range(1981, 2021),
                              numericTimeKeys=True,
                              columns='series').reset_index()

# GIVE COLUMNS APPROPRIATE NAMES
dataframe.rename(columns={'economy': 'Country',
                          'time': 'Year',
                          'EN.ATM.CO2E.KT': 'C2O Emission',
                          'EN.CO2.MANF.ZS': 'C2O Emission From Manufacturers'},
                 inplace=True)

dataframe['C2O Emission'] = dataframe['C2O Emission'].fillna(0)
dataframe['C2O Emission From Manufacturers'] = dataframe[
    'C2O Emission From Manufacturers'].fillna(0)

dataframe.drop('Year', inplace=True, axis=1)

print(dataframe.describe())
print(dataframe.corr())
print()

dataframe = norm_df(dataframe)
print(dataframe.describe())
print()

# CALLING FUNCTION TO CREATE PLOT
makeplot(dataframe,
         "C2O Emission",
         "C2O Emission From Manufacturers")

# EXTRACT COLUMNS FOR FITTING
dataframe_fit = dataframe[["C2O Emission",
                           "C2O Emission From Manufacturers"]].copy()

# DEFINING NUMBER OF CLUSTERS
no_of_clusters = 8

# SETTING UP AGGLOMERATIVE CLUSTERING
ac = cluster.AgglomerativeClustering(n_clusters=no_of_clusters)
ac.fit(dataframe_fit)
labels = ac.labels_

xcen = []
ycen = []
for ic in range(no_of_clusters):
    xc = np.average(dataframe_fit["C2O Emission"][labels == ic])
    yc = np.average(dataframe_fit["C2O Emission From Manufacturers"]
                    [labels == ic])
    xcen.append(xc)
    ycen.append(yc)

# PLOT USING THE LABELS TO SELECT COLOR
plt.figure(figsize=(5.0, 5.0))

col = ["blue",
       "red",
       "green",
       "magenta",
       "yellow",
       "orange",
       "purple",
       "cyan",
       "black"
       ]

for i in range(0, no_of_clusters):
    plt.plot(dataframe_fit["C2O Emission"][labels == i],
             dataframe_fit["C2O Emission From Manufacturers"][labels == i],
             "o",
             markersize=3,
             color=col[i])

for ic in range(no_of_clusters):
    plt.plot(xcen[ic], ycen[ic], "dk", markersize=10)

plt.xlabel("C2O Emission")
plt.ylabel("C2O Emission From Manufacturers")
plt.show()

# WRITING LABELS INTO dataframe, SORTING & EXPORTING AS EXCEL FILE
dataframe["labels"] = labels
dataframe = dataframe.sort_values(["labels"], ignore_index=True)
dataframe.to_excel("co2_clusters.xlsx")
