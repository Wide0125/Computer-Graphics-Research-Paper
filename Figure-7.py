import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.rcParams['text.usetex'] = True

fig, ax = plt.subplots()

ax.add_patch(patches.Rectangle((0, -1080), 1920, 1080, linewidth=1, facecolor='blue', alpha=0.5))
ax.set_xlim(0, 1920)
ax.set_ylim(-1080, 0)

ax.text(0, 0, "(0, 0)", ha='center', va='center', size='x-large')
ax.text(0, -1079, "(0, 1079)", ha='center', va='center', size='x-large')
ax.text(1919, 0, "(1919, 0)", ha='center', va='center', size='x-large')
ax.text(1919, -1079, "(1919, 1079)", ha='center', va='center', size='x-large')

ax.set_box_aspect(9/16)
ax.set_axis_off()

plt.savefig('Figure-7.svg', bbox_inches='tight')

plt.show()
