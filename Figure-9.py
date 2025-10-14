import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True

fig = plt.figure()

ax = fig.add_subplot(projection="3d")
ax.view_init(elev=-21, azim=153, roll=-79.5)
ax.set_box_aspect((1, 1, 1), zoom=1.5)

ax.set_xlim3d(-1, 2)
ax.set_ylim3d(-1, 2)
ax.set_zlim3d(-1, 2)

x, y, z = np.array([[-1,0,0],[0,-1,0],[0,0,-1]])
u, v, w = np.array([[1,0,0],[0,1,0],[0,0,1]])
ax.quiver(x,y,z,u,v,w,arrow_length_ratio=0.1, color="black", length=3)

ax.text(1.9, 0.1, 0, '$x$', size='x-large')
ax.text(0, 1.9, 0.1, '$y$', size='x-large')
ax.text(0, 0.1, 1.9, '$z$', size='x-large')

ax.quiver(0, 0, 0, 0, 1, 1, arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 1, 1, 1, arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, 1, -1, arrow_length_ratio=0.1, color='red')



ax.set_axis_off()

plt.savefig('Figure-9.svg', bbox_inches='tight')

plt.show()
