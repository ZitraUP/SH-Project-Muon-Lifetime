import numpy as np
import scipy
import matplotlib.pyplot as plt
import os
import scipy.integrate as integrate
import scipy.special as special



def FittingEq(t, tau, N_0, b):                       # stes format for fitting eq
    return N_0 * np.exp(-t / tau) + b


def DataCollation():                                # Function to read muon data from a file and collate into a single array
    os.chdir(r'D:\Uni Stuff\4th Year\SH Project')
    print("The Current working directory is: {0}".format(os.getcwd()))

    run1 = np.loadtxt('run1.txt')
    run2 = np.loadtxt('run2.txt')
    run3 = np.loadtxt('run3.txt')
    run4 = np.loadtxt('run4.txt')

    Total = np.concatenate((run1, run2, run3, run4), axis = 0, dtype= float)
    out_tup = [i for i in Total if i[0] <= 20000 and i[0] >= 600]        # limits data array to the desired predeterimined data range
    #print(len(out_tup))
    return out_tup

def Plotting():
    out_tup = DataCollation()                                 # PLotting function. Creates histogram of data and residual plot
    out_tup = np.delete(out_tup, 1, 1)                        #deletes the unwanted column of data
    bin_number= 97
    binnumberDoF = bin_number-3
    n, bins, col = plt.hist(out_tup, bins= bin_number, color= 'skyblue',  ec='black', lw = 0.5) #for histogram plot
    a = np.histogram(out_tup, bins= bin_number) #produces heights & bin centres
    plt.xlabel("Time Between Scintillations /ns")
    plt.ylabel("Frequency")
    plt.title("Histogram showing the frequency of each muon scintillation timestep" "\n" "for the primary data set")

    heights = a[0]
    binedges = a[1]
    bincentres = binedges[:-1] + np.diff(binedges) / 2


    sigmas = np.sqrt(a[0])
    Param_est = [1500, 20000, 150]
    popt, popcov = scipy.optimize.curve_fit(FittingEq, bincentres, heights, sigma=sigmas, p0= Param_est, method= 'lm')   #optimize fitting eq. to find best values for free paramters
    x_points = np.linspace(0, binedges[-1], 15000)
    print(popt)
    print(popcov)


    plt.plot(x_points, FittingEq(x_points, *popt), color= 'green')
    print('mean  muon lifetime (ns) is:')
    print(popt[0])
    print('with error')
    print(np.sqrt(popcov[0,0]))
    print('error on N_0' )
    print(np.sqrt(popcov[1,1]))
    print('error on B' )
    print(np.sqrt(popcov[2,2]))

    print('Chi-Squared (/size of bin) =')
    print(np.sum(((heights - FittingEq(bincentres, *popt)) ** 2) / FittingEq(bincentres, *popt))/(binnumberDoF))
    plt.show()
    residuals = heights - FittingEq(bincentres, *popt)
    y = 0 * x_points
    plt.scatter(binedges[:-1], residuals, marker="x", s=50)
    plt.errorbar(binedges[:-1], residuals, yerr= sigmas,fmt="x")
    plt.xlabel('Time /ns')
    plt.ylabel('Residual')
    plt.title('Plot showing the residual data for the primary data set')
    plt.plot(x_points, y)
    plt.show()

    t_obvs = popt[0]
    t_minus = 2043
    ro = 1.2766
    t_pos = (t_obvs*t_minus*ro) / (t_minus+(ro*t_minus)-t_obvs)   #final extraction of tau
    t_positive = float(t_pos)*1E-9
    print('The lifetime of the positive muon is:', t_positive, "\u03BCs" )



Plotting() #run
