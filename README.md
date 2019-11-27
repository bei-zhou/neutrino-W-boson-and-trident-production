# Neutrino-nucleus cross sections for W-boson and trident production
Here we provide the data files of the cross sections for different neutrino flavors and different nucleus targets. More data files will be uploaded later.   
If you need any more data files not shown here yet, or if you have any other questions, please feel free to contact me:  
    (**Bei Zhou**, beizhousuper@gmail.com).  
Reference papers are https://arxiv.org/abs/1910.08090 and https://arxiv.org/abs/1910.10720 .


## Conventions of the file names

**Neutrino flavors**: ``ve``: \nu_e,  ``vm``: \nu_\mu,   ``vl``: \nu_\tau   
**Charged lepton**: ``e``: e^-,  ``E``: e^+,  ``m``: \mu^-,  ``M``: \mu^+,  ``l``: \tau^- ,  ``L``: \tau^+ ,  
**Nucleus target**: ``O16``: Oxygen 16, ``H1`` Hydrogen 1, (adding O16 and two H1's gives the cross section for water/ice target), ``Fe``: iron, which combines all the major isotopes (Fe54, Fe56, Fe57, Fe58) 
``W``: W boson  
``X``: the final-state of the nucleus part  
``tot``: means total cross section, which sums up all the three scattering regimes (coherent, diffractive, and inelastic regimes; see the references papers above for details).  

Therefore, for example, ``veO16TOeWX_tot.dat`` is for the channel ``\nu_e  O16 -> e^-  W^+  X``.  

Neutrino- and antineutrino-induced channels have the same cross sections. See the references papers above for details.  


## Units
First column: neutrino energy  [ GeV ]  
Second column: cross section  [ cm^2 ]


## Basic usage

If you use python, the files can be read and plotted by the script below  
```python
from numpy import *
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 7), facecolor='w')
ax = fig.add_axes([0.145, 0.12, 0.82, 0.82 ])
ax.set_xscale('log'); ax.set_yscale('log')

xsec = loadtxt('veO16TOeWX_tot.dat').T
ax.plot(xsec[0], xsec[1],'k-',lw=1.5)

plt.show()
```
