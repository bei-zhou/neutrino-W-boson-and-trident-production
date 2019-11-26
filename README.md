# Neutrino-nucleus cross sections for W-boson and trident production
Here we provide the data files for the cross sections, for different neutrino flavor, different nucleus target. More data files will be uploaded later.
If you need any more data files not shown here yet, or if you have any other questions, please feel free to contact me (Bei Zhou, beizhousuper@gmail.com).  
Relevant papers are https://arxiv.org/abs/1910.08090 and https://arxiv.org/abs/1910.10720 .


## Conventions for the files

Neutrino flavors: ``ve``: \nu_e,  ``vm``: \nu_\mu,   ``vl``: \nu_\tau

Charged lepton: ``e``: electron,  ``m``: muon,  ``l``: tau

Nucleus target: ``O16``: Oxygen 16

``W``: W boson

``X``: the final-state of the nucleus part

Therefore, for example, ``veO16TOeWX_tot.dat`` is for the channel ``\nu_e + O16 -> electron + W + X``

The charge signs are suppred because neutrino- and antineutrino-induced channels have the same total and differential cross sections. See https://arxiv.org/abs/1910.08090 for details.


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
