def zeller(day, month, year):
    # Function to evaluate the weekday using Zeller's algorithm. The result
    # is returned in a string containing the weekday.
    # Arguments:
    # 1: day, integer
    # 2: month, integer
    # 3: year, integer

    # conversion into the input of Zeller's algorithm
    zday = day
    zmonth = month - 2
    zyear = year
    # special treatment of Jan and Feb
    if zmonth < 1:
        zmonth = zmonth + 12
        zyear = zyear - 1

    zcent = zyear // 100           # integer division
    zyear = zyear - 100 * zcent    # also possible: zyear = zyear%100
    # calculating the weekday number
    w = (13 * zmonth - 1) // 5
    x = zyear // 4
    y = zcent // 4
    z = w + x + y + zday + zyear - 2 * zcent
    r = z % 7        # remainder of integer division

    # deal with negative values
    if r < 0:
        r = r + 7
    # Conversion of day number into name of the day.
    # Using dictionaries
    weekdays = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
        }

    wkday = weekdays[r]
    return wkday


# reads the datestring
date = input("Please enter the data in the DD/MM/YYYY format: ")

# splits into 3 strings
sday, smonth, syear = date.split("/")

# converts into int
day = int(sday)
month = int(smonth)
year = int(syear)


print(zeller(day, month, year))
