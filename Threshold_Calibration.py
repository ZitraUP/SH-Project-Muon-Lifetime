import scipy
import matplotlib.pyplot as plt
import os
import numpy as np
import math

os.chdir(r'D:\Uni Stuff\4th Year\SH Project')
print("The Current working directory is: {0}".format(os.getcwd()))

Threshold_data = np.loadtxt('Threshold_calibration.txt')
print(Threshold_data)
y_error = np.sqrt(np.delete(Threshold_data, 0, 1)) #isolates single column in .txt file and roots each value
print(y_error.shape)
yerr = np.reshape(y_error, 9)
print(yerr.shape)
#print(*zip(*Threshold_data))
plt.scatter(*zip(*Threshold_data))
plt.errorbar(*zip(*Threshold_data), yerr= yerr, ls='none') #plotting
plt.xlabel('Threshold Voltage /mV')
plt.ylabel('Muon Rate /cpm')
plt.title('Variation of Muon Rate with Threshold Voltage', wrap=True)

plt.show()