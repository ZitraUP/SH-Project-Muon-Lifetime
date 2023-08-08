import numpy as np
import matplotlib.pyplot as plt
import os
#simple code to read and plot data from txt file
os.chdir(r'D:\Uni Stuff\4th Year\SH Project')
print("The Current working directory is: {0}".format(os.getcwd()))

PlateData = np.loadtxt('PlateData.txt')
print(PlateData)

plt.scatter(*zip(*PlateData))
plt.xlabel("Muon Momentum /MeV")
plt.ylabel("Counts /(Mev/c)")
plt.title("A plot of the energy distribution of cosmic-ray muons at sea-level")
plt.show()