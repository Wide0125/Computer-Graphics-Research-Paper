import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'Computer Modern'

fig, ax = plt.subplots()

ax.set_xlim(-0.1, 3)
ax.set_ylim(-0.1, 3)
ax.set_box_aspect(1)

ax.arrow(0, 0, 0, 3, head_width = 0.02, length_includes_head=True, color='black')

ax.text(0.025, 2.9, '$y$', size='x-large')

ax.arrow(0, 0, 3, 0, head_width = 0.02, length_includes_head=True, color='black')

ax.text(2.9, 0.025, '$x$', size='x-large')

plt.arrow(0, 0, 2, 1, head_width=0.1, color='black', length_includes_head=True)

y = np.linspace(0, 1, 100)
x = np.full_like(y, 2)

plt.plot(x, y, color='blue')
plt.text(2.05, 0.5, "$1\hat{\jmath}$", color='blue', size='x-large')

x = np.linspace(0, 2, 100)
y = np.full_like(x, 0)

plt.plot(x, y, color='red')
plt.text(1, -0.2, "$2\hat{\imath}$", color='red', size='x-large')

ax.set_axis_off()

plt.savefig('vectorUnits.svg', bbox_inches='tight')

plt.show()
