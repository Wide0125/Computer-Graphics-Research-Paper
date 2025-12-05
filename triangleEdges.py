import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'Computer Modern'

fig, ax = plt.subplots()

ax.set_xlim(0.1, 2)
ax.set_ylim(0.1, 2)
ax.set_box_aspect(1)

p1 = (1.052, 1.714)
p2 = (1.74, 0.98)
p3 = (0.67, 0.25)

x = np.linspace(p1[0], p2[0], 100)
slope = (p1[1] - p2[1]) / (p1[0] - p2[0])
y = x * slope - p1[0] * slope + p1[1]
ax.plot(x, y, color = 'blue')

x = np.linspace(p1[0], p3[0], 100)
slope = (p1[1] - p3[1]) / (p1[0] - p3[0])
y = x * slope - p1[0] * slope + p1[1]
ax.plot(x, y , color = 'red')

x = np.linspace(p2[0], p3[0], 100)
slope = (p2[1] - p3[1]) / (p2[0] - p3[0])
y = x * slope - p2[0] * slope + p2[1]
ax.plot(x, y, color = 'blue')

ax.plot(p1[0], p1[1], marker='o', color='black')
ax.text(p1[0] + 0.03, p1[1] + 0.03, '$P_1$', size='large')
ax.plot(p2[0], p2[1], marker='o', color='black')
ax.text(p2[0] + 0.03, p2[1], '$P_2$', size='large')
ax.plot(p3[0], p3[1], marker='o', color='black')
ax.text(p3[0], p3[1] - 0.12, '$P_3$', size='large')

ax.text(0.53, 1.034, "Left Edge", color='red')
ax.text(1.5, 1.247, "Right Edge", color='blue')

ax.set_axis_off()

plt.savefig('triangleEdges.svg', bbox_inches='tight')

plt.show()
