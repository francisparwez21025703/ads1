import numpy as np


def vol_radius(r):

    vol = float(4 / 3 * np.pi * r ** 3)
    return vol


def vol_diameter(d):

    vol = float(4 / 3 * np.pi * (d / 2) ** 3)
    return vol


if __name__ == "__main__":
    x = float(input("Enter Radius Or Diameter "))
    choice = input("Enter r For Radius Or d For Diameter ")

    if choice == "r":
        print("The volume is", vol_radius(x))
    elif choice == "d":
        print("The volume is", vol_diameter(x))
