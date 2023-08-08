import scipy
import matplotlib.pyplot as plt
import os
import numpy as np
#EXACT SAME AS FOR Threshold_Calibration
os.chdir(r'D:\Uni Stuff\4th Year\SH Project')
print("The Current working directory is: {0}".format(os.getcwd()))

Voltage_data = np.loadtxt('Voltage_calibration1.txt')
print(Voltage_data)
y_error = np.sqrt(np.delete(Voltage_data, 0, 1))
print(y_error)
yerr = np.reshape(y_error, 12)
print(yerr.shape)
plt.scatter(*zip(*Voltage_data))
plt.errorbar(*zip(*Voltage_data), yerr = yerr, ls ='none')
plt.xlabel('PMT Voltage /V')
plt.ylabel('Muon Rate /cpm')
plt.title('Variation of Muon Rate with PMT Voltage', wrap=True)

plt.show()