import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sys
try:
    import vplot as vpl
except:
    print('Cannot import vplot. Please install vplot.')

# Check correct number of arguments
if (len(sys.argv) != 2):
    print('ERROR: Incorrect number of arguments.')
    print('Usage: '+sys.argv[0]+' <pdf | png>')
    exit(1)
if (sys.argv[1] != 'pdf' and sys.argv[1] != 'png'):
    print('ERROR: Unknown file format: '+sys.argv[1])
    print('Options are: pdf, png')
    exit(1)

plotfile="MuAraeSpiNBody"

#Typical plot parameters that make for pretty plot
mpl.rcParams['figure.figsize'] = (10,8)
mpl.rcParams['font.size'] = 16.0

# Load data
output = vpl.GetOutput()

# Extract data
time = output.star.Time/1.0e6 # Scale to Myr
eccb = output.b.Eccentricity
eccc = output.c.Eccentricity
eccd = output.d.Eccentricity
ecce = output.e.Eccentricity
incb = output.b.SpiNBodyInc
incc = output.c.SpiNBodyInc
incd = output.d.SpiNBodyInc
ince = output.e.SpiNBodyInc

etot = (output.star.TotOrbEnergy/output.star.TotOrbEnergy[0] - 1)*1e9
jtot = (output.star.TotAngMom/output.star.TotAngMom[0] - 1)*1e11

# Plot
fig, axes = plt.subplots(nrows=3, ncols=1)
color = "k"

## Top: Eccentricity ##
axes[0,0].plot(time,ecce,color='k')
axes[0,0].plot(time,eccb,color=vpl.colors.dark_blue)
axes[0,0].plot(time,eccc,color=vpl.colors.pale_blue)
axes[0,0].plot(time,eccd,color=vpl.colors.orange)

# Format
axes[0,0].set_xlim(time.min(),time.max())
#axes[0,0].legend(loc="best")
axes[0,0].set_ylim(0,1)
axes[0,0].set_xlabel("Time [Myr]")
axes[0,0].set_ylabel("Eccentricity")
#axes[0,0].set_xticks([0, 2.5, 5, 7.5, 10])
#axes[0,0].set_xticklabels(["0", "2.5", "5","7.5", "10"])

## Middle: Inclination ##
axes[0,1].plot(time, ince,'k')
axes[0,1].plot(time, incb, color=vpl.colors.dark_blue)
axes[0,1].plot(time, incc, color=vpl.colors.pale_blue)
axes[0,1].plot(time, incd, color=vpl.colors.orange)

# Format
axes[0,1].set_xlim(time.min(),time.max())
axes[0,1].set_ylim(0.0,10)
axes[0,1].set_xlabel("Time [Myr]")
axes[0,1].set_ylabel("Inclination [$^\circ$]")
#axes[0,1].set_xticks([0, 0.25, 0.5, 0.75, 1])
#axes[0,1].set_xticklabels(["0", "0.25", "0.5","0.75", "1"])
#axes[0,1].set_yticks([0, 0.5, 1])
#axes[0,1].set_yticklabels(["0", "0.5", "1"])

## Bottom: E,J Conservation ##
axes[2,1].plot(time,etot,color=vpl.colors.red,label=(r'Energy $\times 10^9$'))
axes[2,1].plot(time,jtot,color=vpl.colors.purple,label=(r'Ang. Mom. $\times 10^{11}$'))

# Format
axes[2,1].set_xlim(time.min(),time.max())
axes[2,1].set_ylim(-1.1,1.11)
axes[2,1].legend(loc='best',fontsize=12)
axes[2,1].set_xlabel("Time [Myr]")
axes[2,1].set_ylabel(r"$\Delta$E,  $\Delta$J")
#axes[2,1].set_xticks([0, 0.25, 0.5, 0.75, 1])
#axes[2,1].set_xticklabels(["0", "0.25", "0.5","0.75", "1"])

# Final formating
fig.tight_layout()

if (sys.argv[1] == 'pdf'):
    plotfile += ".pdf"
if (sys.argv[1] == 'png'):
    plotfile += ".png"

fig.savefig(plotfile, bbox_inches="tight", dpi=600)

print('Wrote '+plotfile+'.')
