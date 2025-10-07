import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True

fig = plt.figure()

ax = fig.add_subplot(projection="3d")
ax.view_init(elev=-21, azim=153, roll=-79.5)
ax.set_box_aspect((1, 1, 1), zoom=1.3)

ax.set_xlim3d(-1, 4)
ax.set_ylim3d(-1, 4)
ax.set_zlim3d(-1, 4)

x, y, z = np.array([[-1,0,0],[0,-1,0],[0,0,-1]])
u, v, w = np.array([[1,0,0],[0,1,0],[0,0,1]])
ax.quiver(x,y,z,u,v,w,arrow_length_ratio=0.1, color="black", length=5)

ax.text(3.9, 0.1, 0, '$x$', size='x-large')
ax.text(0, 3.9, 0.1, '$y$', size='x-large')
ax.text(0, 0.1, 3.9, '$z$', size='x-large')

ax.plot([0, 1], [0, 2], [0, 3], marker='o')
ax.quiver(0,0,0,1,0,0,arrow_length_ratio=0.1, color="red", length=1, linewidths=3)
ax.text(0.1, 0, -0.4, '$1$', size='x-large', zdir='x', ha='center', color='red')
ax.quiver(1,0,0,0,2,0,arrow_length_ratio=0.1, color="green", length=1, linewidths=3)
ax.text(1, 1, -0.3, '$2$', size='x-large', zdir='y', ha='center', color='green')
ax.quiver(1,2,0,0,0,3,arrow_length_ratio=0.1, color="blue", length=1, linewidths=3)
ax.text(1, 2.1, 1.5, '$3$', size='x-large', ha='center', color='blue')


ax.set_axis_off()

plt.savefig('Figure-4.svg', bbox_inches='tight')

plt.show()
