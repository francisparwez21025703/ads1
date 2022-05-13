#!/usr/bin/env python
# coding: utf-8

# ### Exercise 1
# 
# Import modules, read the csv file ahd check its content.

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt


# read file into dataframe and print
df_countries = pd.read_csv("countries_top10.csv")
print(df_countries)
print()


# Calculate new columns and write into Excel file. Open the Excel file and have a look.

# In[ ]:


# calculate GDP per head and population per km^2
df_countries["GDP/head"] = df_countries["GDP"] / df_countries["Population"]
df_countries["Pop/km^2"] = df_countries["Population"] / df_countries["Area"]
print(df_countries)

# write into Excel file
df_countries.to_excel("countries_top10.xlsx")


# Now the plot. `"bo"` is indicating blue circles.

# In[ ]:


# scatter plot
plt.figure()

plt.plot(df_countries["Population"], df_countries["GDP"], "bo")

plt.xlabel("Population", fontsize=12)
plt.ylabel("GDP", fontsize=12)
plt.title("Top 10 most populous countries", size=15)

plt.xlim(0.0, 1.5e9)

plt.show()


# ### Exercise 2

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt


# read file into dataframe and print
df_gdp = pd.read_excel("GDP_2015dollars.xls")
print(df_gdp)
print()

# line plots
plt.figure()

# plot the four countries with labels
plt.plot(df_gdp["Year"], df_gdp["China"], "b-", label="China")
plt.plot(df_gdp["Year"], df_gdp["Germany"], "g:", label="Germany")
plt.plot(df_gdp["Year"], df_gdp["Japan"], "r--", label="Japan")
plt.plot(df_gdp["Year"], df_gdp["United States"], "k-.", label="USA")

# set labels and show the legend
plt.xlabel("Year")
plt.ylabel("GDP (2015 $)")
plt.legend()

plt.show()


# In[ ]:





# In[ ]:




