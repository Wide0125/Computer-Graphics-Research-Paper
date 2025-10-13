import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True

fig = plt.figure()

ax = fig.add_subplot(projection="3d", computed_zorder=False)
ax.view_init(elev=-21, azim=153, roll=-79.5)
ax.set_box_aspect((1, 1, 1), zoom=1.5)

ax.set_xlim3d(-1, 2)
ax.set_ylim3d(-1, 2)
ax.set_zlim3d(-1, 2)

x, y, z = np.array([[-1,0,0],[0,-1,0],[0,0,-1]])
u, v, w = np.array([[1,0,0],[0,1,0],[0,0,1]])
ax.quiver(x,y,z,u,v,w,arrow_length_ratio=0.1, color="black", length=3, zorder=1)

ax.text(1.9, 0.1, 0, '$x$', size='x-large')
ax.text(0, 1.9, 0.1, '$y$', size='x-large')
ax.text(0, 0.1, 1.9, '$z$', size='x-large')

x = np.array([np.linspace(-0.5/9*16, 0.5/9*16, 1920)] * 1080)
y = np.rot90(np.array([np.linspace(-0.5, 0.5, 1080)] * 1920))
z = np.full((1080, 1920), 1)

ax.plot_surface(x, y, z, color='gray', rcount=1, ccount=1, alpha=1, zorder=3)

ax.quiver(0, 0, 0, 0, 0, 1, arrow_length_ratio=0, color='black', zorder=4)

ax.quiver(0, 0, 0, 0.5/9*16, 0.5, 1, arrow_length_ratio=0.1, color='red', linewidths=3, alpha = 1, zorder=3)

ax.set_axis_off()

plt.savefig('Figure-6.svg', bbox_inches='tight')

plt.show()
