import numpy as np
import scipy
import matplotlib.pyplot as plt
import os
import scipy.integrate as integrate
import scipy.special as special

#CODE WORKS IN EXACTLY THE SAME WAY AS MuonLifetime but for a specific large data set

def FittingEq(t, tau, N_0, b):                                                              # sts format fir fitting eq
    return N_0 * np.exp(-t / tau) + b


def DataCollation():                                                                          # Function to read muon data from a file and collate into a single array
    os.chdir(r'D:\Uni Stuff\4th Year\SH Project')
    print("The Current working directory is: {0}".format(os.getcwd()))

    Total = np.loadtxt('Big_data.txt')
    out_tup = [i for i in Total if i[0] <= 20000 and i[0] >= 800]  # limits data array to the desired predeterimined data range
    print(len(out_tup))
    return out_tup

def Plotting():
    out_tup = DataCollation()                                                                  # PLotting function. Creates histogram of data and residual plot
    out_tup = np.delete(out_tup, 1, 1)
    bin_number = 96
    binnumberDOF = bin_number-3
    n, bins, col = plt.hist(out_tup, bins=bin_number, color='skyblue', ec='black', lw=0.5)
    a = np.histogram(out_tup, bins=bin_number)
    plt.xlabel("Time between Scintillations /ns")
    plt.ylabel("Frequency")
    plt.title("Histogram showing the Frequency of each muon scintillation timestep" "\n" "for the secondary data set")

    heights = a[0]
    binedges = a[1]
    bincentres = binedges[:-1] + np.diff(binedges) / 2

    sigmas = np.sqrt(a[0])
    Param_est = [1500, 20000, 150]
    popt, popcov = scipy.optimize.curve_fit(FittingEq, bincentres, heights, sigma=sigmas, p0=Param_est, method='lm')
    x_points = np.linspace(500, binedges[-1], 15000)
    print(popt)
    print(np.sqrt(popcov[1,1]))
    print(np.sqrt(popcov[2, 2]))
    plt.plot(x_points, FittingEq(x_points, *popt), color='green')
    print('mean  muon lifetime (ns) is:')
    print(popt[0])
    print('with error')
    print(np.sqrt(popcov[0, 0]))
    print('Chi-Squared (/size of bin) =')
    print(np.sum(((heights - FittingEq(bincentres, *popt)) ** 2) / FittingEq(bincentres, *popt)) / binnumberDOF)
    plt.show()
    residuals = heights - FittingEq(bincentres, *popt)
    y = 0 * x_points
    plt.scatter(binedges[:-1], residuals, marker="x", s=50)
    plt.errorbar(binedges[:-1], residuals, yerr= sigmas,fmt="x")
    plt.xlabel('Time /ns')
    plt.ylabel('Residual')
    plt.title('Plot showing the residual data for the secondary data set')
    plt.plot(x_points, y)
    plt.show()

    t_obvs = popt[0]
    t_minus = 2043
    ro = 1.2766
    t_pos = (t_obvs * t_minus * ro) / (t_minus + (ro * t_minus) - t_obvs)
    t_positive = float(t_pos) * 1E-9
    print('The lifetime of the positive muon is:', t_positive, "\u03BCs")


Plotting()
