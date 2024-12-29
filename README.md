# Cross sections of the neutrino-nucleus W-boson production (WBP) and trident production

Here, we provide the data files for the cross sections and differential cross sections for different neutrino flavors and different nucleus targets. More data files will be uploaded later.

If you need any data not shown here yet, or if you have any questions, please feel free to contact me -- I'd be happy to help you!
    (**Bei Zhou**, beizhousuper@gmail.com).  

When you use the data for publications, please cite https://arxiv.org/abs/1910.08090 and https://arxiv.org/abs/1910.10720 by Bei Zhou and John F. Beacom (if there is a limit on reference number, you may cite the former only). 
The first paper developed the theoretical framework and calculated the total cross sections. The second paper calculated differential cross sections, d\sigma/d_E, and studied the phenomenological consequences like neutrino absorptions in the Earth and detections in the TeV-PeV observatories like IceCube and IceCube-Gen2.

## Updates on July 13, 2023, WBP cross sections (./W_boson_production_cross_section):
The calculation of the inelastic component of the WBP cross section now uses the latest (second-generation) photon PDFs of proton and neutron from CT18qed (https://cteq-tea.gitlab.io/project/00pdfs/).  In the previous work (https://arxiv.org/abs/1910.08090), we used the (first-generation) CT14qed photon PDFs. The WBP inelastic cross section from CT18qed is **10--30% higher** than that from CT14qed.

Also, in the WBP cross section files, we added a third column that has the cross section uncertainty, including the uncertainties of the 1) coherent component, 2) diffractive component, 3) inelastic component, PDF uncertainty, and 4) inelastic component, scale uncertainty.

More details can be found in Fig. 20 and relevant text in https://arxiv.org/abs/2305.10497 by Keping Xie, Bei Zhou, and T. J. Hobbs.

## Updates on December 20, 2024, WBP differential cross sections (./W_boson_production_differential_cross_section):
We uploaded the differential cross section data and some figures. 

If you need to interpolate over the data, be careful when dealing with those near the right end at large Enu, where the numbers increase quickly.

All the differential cross section files are for the charged lepton, i.e., d\sigma/dE_\ell. The differential cross section of the W boson can be easily obtained using E_W = E_\nu - E_\ell, because the energy that goes to the nucleus is negligible.  If you simulate events based on the files, you can simulate E_\ell first and then get the simulated E_W simply through E_W = E_\nu - E_\ell. 

Note that neutrino and antineutrino have the same cross sections and differential cross sections.


## Conventions of the file names

**Neutrino flavors**:  
``nue`` or ``ve``: \nu_e  
``numu`` or ``vm``: \nu_\mu  
``nutau`` or ``vl``: \nu_\tau  

**Nucleus targets**:  
``H2O``: water/ice.  
``Fe``: iron, which combines all the major isotopes (Fe54, Fe56, Fe57, Fe58), which matters for neutrino in-earth absorption.  
``EarthAvg``: Earth's averaged (by number density) chemical composition, which matters for neutrino in-earth absorption.  
``O16``: Oxygen 16.  
``H1``: Hydrogen 1 (adding O16 and two H1's gives the cross section for water/ice target).  

**Charged leptons**:  
In the ``W_boson_production`` folder:  
``e``: e^- or e^+  
``mu``: \mu^- or \mu^-  
``tau``: \tau^- or \tau^+     

In the ``trident_production`` folder:  
``e``: e^-  
``E``: e^+  
``m``: \mu^-  
``M``: \mu^+  
``l``: \tau^-  
``L``: \tau^+     

**Others**:  
``W``: W boson  
``X``: the final-state of the nucleus part    
``tot``: means total cross section, which sums up all the three scattering regimes/components (coherent component, diffractive component for proton and neutron, and inelastic component for proton and neutron; see the references papers above for details).  
Therefore, for example, ``nue_H2O_TO_e_W_X_tot.txt`` is for the channel ``\nu_e  H_2O -> e^-  W^+  X`` or ``\bar{\nu}_e  H_2O -> e^+  W^-  X``.  
Neutrino- and antineutrino-induced channels have the same cross sections. See the references papers above for details.  


## Units of the data
First column: neutrino energy  [ GeV ]  
Second column: cross section  [ cm^2 ]  
Third column (for WBP only): relative uncertainty of the cross section (the thrid column times the second column gives the absolute cross section uncertainty in cm^2).


## Basic usage

If you use python, the files can be read and plotted by the script below  
```python
from numpy import *
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 7), facecolor='w')
ax = fig.add_axes([0.145, 0.12, 0.82, 0.82 ])
ax.set_xscale('log'); ax.set_yscale('log')

xsec = loadtxt('W_boson_production/nue_H2O_TO_e_W_X_tot.txt').T
ax.plot(xsec[0], xsec[1],'r-',lw=1.5)
ax.fill_between(xsec[0], xsec[1]*(1-xsec[2]), xsec[1]*(1+xsec[2]), facecolor='r', alpha=0.3)

plt.show()
```
