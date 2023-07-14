#!/usr/bin/python
from numpy import *
import matplotlib.pyplot as plt 


fig = plt.figure(figsize=(8, 8), facecolor='w')
ax = fig.add_axes([0.145, 0.12, 0.82, 0.82 ])

ax.set_xscale('log'); ax.set_yscale('log')

tmp = loadtxt('W_boson_production/nue_H2O_TO_e_W_X_tot.txt').T
plot = ax.plot(tmp[0], tmp[1], 'r-', label=r'', lw=1.5, ms=3)
ax.fill_between(tmp[0], tmp[1]*(1+tmp[2]), tmp[1]*(1-tmp[2]), facecolor='r', alpha=0.3)
tmp = loadtxt('W_boson_production/numu_H2O_TO_mu_W_X_tot.txt').T
plot = ax.plot(tmp[0], tmp[1], 'r-', label=r'', lw=1.5, ms=3)
ax.fill_between(tmp[0], tmp[1]*(1+tmp[2]), tmp[1]*(1-tmp[2]), facecolor='r', alpha=0.3)
tmp = loadtxt('W_boson_production/nutau_H2O_TO_tau_W_X_tot.txt').T
plot = ax.plot(tmp[0], tmp[1], 'r-', label=r'', lw=1.5, ms=3)
ax.fill_between(tmp[0], tmp[1]*(1+tmp[2]), tmp[1]*(1-tmp[2]), facecolor='r', alpha=0.3)

tmp = loadtxt('W_boson_production/nue_Fe_TO_e_W_X_tot.txt').T
plot = ax.plot(tmp[0], tmp[1], 'g-', label=r'', lw=1.5, ms=3)
ax.fill_between(tmp[0], tmp[1]*(1+tmp[2]), tmp[1]*(1-tmp[2]), facecolor='g', alpha=0.3)
tmp = loadtxt('W_boson_production/numu_Fe_TO_mu_W_X_tot.txt').T
plot = ax.plot(tmp[0], tmp[1], 'g-', label=r'', lw=1.5, ms=3)
ax.fill_between(tmp[0], tmp[1]*(1+tmp[2]), tmp[1]*(1-tmp[2]), facecolor='g', alpha=0.3)
tmp = loadtxt('W_boson_production/nutau_Fe_TO_tau_W_X_tot.txt').T
plot = ax.plot(tmp[0], tmp[1], 'g-', label=r'', lw=1.5, ms=3)
ax.fill_between(tmp[0], tmp[1]*(1+tmp[2]), tmp[1]*(1-tmp[2]), facecolor='g', alpha=0.3)

tmp = loadtxt('W_boson_production/nue_EarthAvg_TO_e_W_X_tot.txt').T
plot = ax.plot(tmp[0], tmp[1], 'b-', label=r'', lw=1.5, ms=3)
ax.fill_between(tmp[0], tmp[1]*(1+tmp[2]), tmp[1]*(1-tmp[2]), facecolor='b', alpha=0.3)
tmp = loadtxt('W_boson_production/numu_EarthAvg_TO_mu_W_X_tot.txt').T
plot = ax.plot(tmp[0], tmp[1], 'b-', label=r'', lw=1.5, ms=3)
ax.fill_between(tmp[0], tmp[1]*(1+tmp[2]), tmp[1]*(1-tmp[2]), facecolor='b', alpha=0.3)
tmp = loadtxt('W_boson_production/nutau_EarthAvg_TO_tau_W_X_tot.txt').T
plot = ax.plot(tmp[0], tmp[1], 'b-', label=r'', lw=1.5, ms=3)
ax.fill_between(tmp[0], tmp[1]*(1+tmp[2]), tmp[1]*(1-tmp[2]), facecolor='b', alpha=0.3)


ax.set_ylabel(r"Cross section  [ cm$^2$ ]",fontsize=20)   
ax.set_xlabel(r"$E_\nu$  [ GeV ]",fontsize=20, labelpad=None)
ax.set_xlim(3e3,1e8); 
ax.set_ylim(1e-39, 1e-31)

plt.legend(loc='best',prop={'size':13}) 
ax.tick_params(axis='both', which='major', direction='in', length = 10, width = 1.5, labelsize=20, right=True, top=True)
ax.tick_params(axis='x', pad=6) # for numbers with superscript, 6 is from adjusting to match y axis
for i in range(1): 
    # fix the issue of ticks missing when axis range > 10 decades
    import matplotlib.ticker 
    #Basically know how it works, not totally
    #Used locmaj_x, _y different because problem happens when using same
    locmaj_x = matplotlib.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=100)
    locmin_x = matplotlib.ticker.LogLocator(base=10.0, subs=arange(2, 10) * .1,
            numticks=100)
    ax.xaxis.set_major_locator(locmaj_x)
    ax.xaxis.set_minor_locator(locmin_x)
    ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())

    locmaj_y = matplotlib.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=100)
    locmin_y = matplotlib.ticker.LogLocator(base=10.0, subs=arange(2, 10) * .1,
            numticks=100)
    ax.yaxis.set_major_locator(locmaj_y)
    ax.yaxis.set_minor_locator(locmin_y)
    ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(axis='both', which='minor', direction='in', length = 5, width = 1, labelsize=20, right=True, top=True)
# for y-aixs ticks
ax.yaxis.get_ticklocs(minor=True)
ax.minorticks_on()
plt.show()




#backup
