import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sys
import subprocess as subp

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

figtype=sys.argv[1]

## Make figures in subdirectories

cmd='cd bde; python makeplot.py '+figtype
subp.call(cmd,shell=True)

cmd='cd be; python makeplot.py '+figtype
subp.call(cmd,shell=True)
