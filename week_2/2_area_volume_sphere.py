import numpy as np

for radius in range(2, 21, 2):
    area = 4.0 * np.pi * radius ** 2
    volume = 4.0 / 3.0 * np.pi * radius ** 3
    print("Radius:", radius, "Area:", area, "Volume:", volume)
