import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import numpy as np

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'Computer Modern'

fig, ax = plt.subplots()

ax.set_xlim(-0.1, 3)
ax.set_ylim(-2.1, 1)
ax.set_box_aspect(1)

ax.arrow(0, 0, 0, 1, head_width = 0.02, length_includes_head=True, color='black')

ax.text(0.025, 0.9, '$y$', size='x-large')

ax.arrow(0, 0, 0, -2, head_width = 0, length_includes_head=True, color='black')

ax.arrow(0, 0, 3, 0, head_width = 0.02, length_includes_head=True, color='black')

ax.text(2.9, 0.025, '$x$', size='x-large')

rotangle = -60
rotMatrix = np.array([[np.cos(np.radians(rotangle)), -np.sin(np.radians(rotangle))], 
[np.sin(np.radians(rotangle)), np.cos(np.radians(rotangle))]])

plt.arrow(0, 0, 2, 1, head_width=0.1, color='black', length_includes_head=True)
plt.text(1, 0.55, "$\\vec{V}$", color='black', size='x-large')

temp = np.matmul(rotMatrix, (1, 0.55))
plt.text(temp[0], temp[1], "$\\vec{V^\prime}$", color='black', size='x-large')

temp = np.matmul(rotMatrix, ([2], [1]))
plt.arrow(0, 0, temp[0][0], temp[1][0], head_width=0.1, color='black', length_includes_head=True)

plt.arrow(2, 0, 0, 1, color='blue', head_width=0.05, length_includes_head=True)
plt.text(2.05, 0.5, "$1\hat{\jmath}$", color='blue', size='x-large')
temp = np.matmul(rotMatrix, (2.05, 0.5))
plt.text(temp[0], temp[1] - 0.1, "$1\hat{\jmath}^\prime$", color='blue', size='x-large')

tempB = np.matmul(rotMatrix, (2, 0))
tempD = np.matmul(rotMatrix, (0, 1))

plt.arrow(tempB[0], tempB[1], tempD[0], tempD[1], color='blue', head_width=0.05, length_includes_head=True)

plt.arrow(0, 0, 1, 0, color='red', head_width=0.05, length_includes_head=True)
tempB = np.matmul(rotMatrix, (0, 0))
tempD = np.matmul(rotMatrix, (1, 0))
plt.arrow(tempB[0], tempB[1], tempD[0], tempD[1], color='red', head_width=0.05, length_includes_head=True)

plt.arrow(1, 0, 1, 0, color='red', head_width=0.05, length_includes_head=True)
tempB = np.matmul(rotMatrix, (1, 0))
tempD = np.matmul(rotMatrix, (1, 0))
plt.arrow(tempB[0], tempB[1], tempD[0], tempD[1], color='red', head_width=0.05, length_includes_head=True)
plt.text(1, -0.2, "$2\hat{\imath}$", color='red', size='x-large')
temp = np.matmul(rotMatrix, (1, -0.2))
plt.text(temp[0], temp[1] - 0.05, "$2\hat{\imath}^\prime$", color='red', size='x-large')

wedge = Wedge((0, 0), 0.3, theta2 = np.degrees(np.atan(0.5)), theta1 = np.degrees(np.atan(0.5)) - 60, color='black', alpha=0.5)
ax.add_patch(wedge)

wedge = Wedge((0, 0), 0.3, theta2 = 0, theta1 = -60, color='red', alpha=0.5)
ax.add_patch(wedge)

ax.set_axis_off()

plt.savefig('vectorTransformation.svg', bbox_inches='tight')

plt.show()
