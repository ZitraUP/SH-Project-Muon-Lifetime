import scipy
import matplotlib.pyplot as plt
import os
import numpy as np
#code to read chi-squared data and plot
os.chdir(r'D:\Uni Stuff\4th Year\SH Project')
print("The Current working directory is: {0}".format(os.getcwd()))

chi_data = np.loadtxt('Chi_squared_raww.txt')
print(chi_data)
plt.scatter(*zip(*chi_data))
plt.xlabel('Starting Point for Scintillation Time /ns')
plt.ylabel('$\u03C7^2$')
plt.title('A plot representing the variation of the $\u03C7^2$ value of the primary data set for various lower bounds', wrap=True)

plt.show()