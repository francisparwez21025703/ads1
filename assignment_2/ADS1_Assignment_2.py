# IMPORTANT LIBRARIES
import pandas as pd
import wbgapi as wb

"""
FUNCTION DEFINITION THAT CREATES & RETURNS A LIST OF 2 DATAFRAME BASED
ON 2 WORLD BANK API's INDICATORS
"""


def make_dataframe(indicator_1, indicator_2):

    country_names = {"GBR": "United Kingdom",
                     "PAK": "Pakistan",
                     "CAN": "Canada",
                     "ITA": "Italy",
                     "BRA": "Brazil",
                     "CHN": "China",
                     "CRI": "Costa Rica",
                     "DNK": "Denmark",
                     "SLV": "El Salvador"}

    dataframe1 = wb.data.DataFrame([indicator_1,
                                   indicator_2],
                                   country_names,
                                   time=range(2000, 2021),
                                   numericTimeKeys=True,
                                   columns='time').reset_index()

    dataframe1.rename(columns={'economy': 'Country Code',
                               'time': 'Year',
                               indicator_1: indicator_1,
                               indicator_2: indicator_2},
                      inplace=True)

    dataframe2 = wb.data.DataFrame([indicator_1,
                                   indicator_2],
                                   country_names,
                                   time=range(2000, 2021),
                                   numericTimeKeys=True,
                                   columns='economy').reset_index()

    dataframe2.rename(columns={'economy': 'Country Code',
                               'time': 'Year',
                               indicator_1: indicator_1,
                               indicator_2: indicator_2},
                      inplace=True)

    return [dataframe1, dataframe2]


"""
FUNCTION THAT RETURNS CORRELATION BETWEEN A SINGLE DATA SERIES
WITH THE DATAFRAME IT IS A PART OF
"""


def correlation_between(dataframe, dataseries):
    return dataframe.corrwith(dataseries)


"""
MAIN EXECUTION THAT INDICATES ENTRY POINT OF THE
CODE
"""

if __name__ == "__main__":
    """
    MAKING DATAFRAMES WITH INDICATORS:
    1) ELECTRICITY PRODUCTION FROM HYDROELECTRIC SOURCES
    2) URBAN POPULATIONS
    """
    dataframe1, dataframe2 = make_dataframe("EG.ELC.HYRO.ZS", "SP.URB.TOTL")

    correlation_with_last_few_rows = []

    """
    FINDING CORRELATION OF THE LAST 5 RECORD WITH EACH RECORD
    INDIVIDUALLY WITH YEARS AS COLUMNS
    """
    for i in range(10):
        correlation_with_last_few_rows.append(
            correlation_between(dataframe1, dataframe1.iloc[:, 0 - (i + 1)]))

    correlation_with_last_few_rows = pd.Series(correlation_with_last_few_rows)
    correlation_with_last_few_rows.hist()

    """
    FINDING CORRELATION OF THE LAST 5 RECORD WITH EACH RECORD
    INDIVIDUALLY WITH COUNTRY CODE AS COLUMNS
    """

    for i in range(10):
        correlation_with_last_few_rows.append(
            correlation_between(dataframe2, dataframe2.iloc[:, 0 - (i + 1)]))

    correlation_with_last_few_rows = pd.Series(correlation_with_last_few_rows)
    correlation_with_last_few_rows.hist()
