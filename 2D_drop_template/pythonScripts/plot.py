#!/bin/python3.8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib
#matplotlib.use('Agg')

t, res = np.loadtxt('logs/p_rgh_2', unpack=True)


fig = plt.figure()#figsize=(11,11))
fig.suptitle(r"Initial residuals $p-\rho gh$", fontsize=16, fontweight='bold')
ax = fig.add_subplot(111)

ax.set_yscale('log')
#ax.set_title("Drop CoM displacement", fontweight='bold')
#ax.set_xlim([-0.025e4,len(deltaT)])
#ax.set_ylim([1.1e-7,2.2e-7])
ax.set_aspect("auto")
#ax.xaxis.set_ticks(np.linspace(0.,1.2e4,7))
#ax.yaxis.set_ticks(np.linspace(1.2e-7,2.2e-7,6))
#ax.xaxis.set_ticks(np.arange(0.,1.2e4,0.05e4), minor=True)
#ax.yaxis.set_ticks(np.arange(1.1e-7,2.2e-7,0.1e-7), minor=True)
ax.set_xlabel('Time [s]', fontsize=10)
ax.set_ylabel("Initial residual", fontsize=10)
ax.grid(which='major', lw=0.5, ls=':')
#ax.grid(which='minor', lw=0.5, ls=':')
#ax.ticklabel_format(axis="both", style="sci", scilimits=(0,0))
ax.tick_params(direction='inout', length=8)
#ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.2e'))
#ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.2e'))

ax.plot(t, res, lw=0.7, color='red')

plt.show()

#fig.savefig('img/res.png', dpi = 1200)
