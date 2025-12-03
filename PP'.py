import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'Computer Modern'

fig, ax = plt.subplots()

ax.set_xlim(-0.1, 2)
ax.set_ylim(-0.5, 2)
ax.set_box_aspect(1)


ax.arrow(0, 0, 0, 2, head_width = 0.02, length_includes_head=True, color='black')

ax.text(0.025, 1.9, '$y$', size='x-large')

ax.arrow(0, 0, 2, 0, head_width = 0.02, length_includes_head=True, color='black')

ax.text(1.9, 0.025, '$z$', size='x-large')

x = np.linspace(0, 1.5, 100)
y = np.full_like(x, 0)

ax.plot(x, y, color='red')

y = np.linspace(-0.5, 0.5, 100)
x = np.full_like(x, 1)

ax.plot(x, y, color='blue')

x = np.linspace(0, 1.5, 100)
y = x * (0.5/1.5)
ax.plot(x, y, color='red')

y = np.linspace(0, 0.5, 100)
x = np.full_like(y, 1.5)
ax.plot(x, y, color='red')

ax.plot(1.5, 0.5, marker='o', color='black')
ax.text(1.55, 0.45, '$P$', size='x-large')

ax.plot(1, 0, marker='o', color='black')
ax.text(1.03, -0.13, "$A'$", size='x-large')

ax.plot(1.5, 0, marker='o', color='black')
ax.text(1.53, -0.13, "$A$", size='x-large')

ax.plot(1, 1/3, marker='o', color='black')
ax.text(1.03, 1/3-0.1, "$P'$", size='x-large')

x = np.linspace(1.5, 1.4, 100)
y = np.full_like(x, 0.1)
ax.plot(x, y, color='black')

y = np.linspace(0, 0.1, 100)
x = np.full_like(x, 1.4)
ax.plot(x, y, color='black')

ax.text(-0.1, -0.1, "$O$", color='black', size='x-large')

ax.text(1.01, 0.45, "Viewport", color='blue')

ax.set_axis_off()

plt.savefig('PP.svg', bbox_inches='tight')

plt.show()
