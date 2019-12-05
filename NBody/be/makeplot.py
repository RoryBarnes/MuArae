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

plotfile="MuAraeSpiNBody_be"

#Typical plot parameters that make for pretty plot
mpl.rcParams['figure.figsize'] = (10,8)
mpl.rcParams['font.size'] = 16.0

# Load data
output = vpl.GetOutput()

# Extract data
time = output.star.Time
#ecc1 = output.d.Eccentricity
ecc2 = output.b.Eccentricity
ecc3 = output.e.Eccentricity
#a1 = output.d.SemiMajorAxis
a2 = output.b.SemiMajorAxis
a3 = output.e.SemiMajorAxis

# Plot
fig, axes = plt.subplots(nrows=2, ncols=1)
color = "k"

## Upper left: a1 ##
#axes[0].plot(time, a1, color='k', label='d')
axes[0].plot(time, a2, color=vpl.colors.pale_blue, label='b')
axes[0].plot(time, a3, color=vpl.colors.red, label='e')
# Format
axes[0].set_xlim(0,2e4)
axes[0].legend(loc="best")
axes[0].set_ylim(0,6)
axes[0].set_xlabel("Time [yr]")
axes[0].set_ylabel("Semi-major Axis [AU]")
#axes[0].set_xticks([0, 0.25, 0.5, 0.75, 1])
#axes[0].set_xticklabels(["0", "0.25", "0.5","0.75", "1"])
#axes[0].set_xscale('log')

## Upper right: eccentricities ##
#axes[1].plot(time, ecc1,'k')
axes[1].plot(time, ecc2, color=vpl.colors.pale_blue)
axes[1].plot(time, ecc3, color=vpl.colors.red)

# Format
axes[1].set_xlim(0,2e4)
axes[1].set_ylim(0.0,0.3)
axes[1].set_xlabel("Time [yr]")
axes[1].set_ylabel("Eccentricity")
#axes[1].set_xticks([0, 0.25, 0.5, 0.75, 1])
#axes[1].set_xticklabels(["0", "0.25", "0.5","0.75", "1"])
#axes[1].set_yticks([0,0.3])
#axes[1].set_yticklabels(["0", "1", "2"])
#axes[1].set_xscale('log')

# Final formating
fig.tight_layout()

if (sys.argv[1] == 'pdf'):
    plotfile += ".pdf"
if (sys.argv[1] == 'png'):
    plotfile += ".png"

fig.savefig(plotfile, bbox_inches="tight", dpi=600)

print('Wrote '+plotfile+'.')
