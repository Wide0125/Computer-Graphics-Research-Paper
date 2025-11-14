import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True

fig = plt.figure()

ax = fig.add_subplot(projection="3d")
ax.view_init(elev=-21, azim=153, roll=-79.5)
ax.set_box_aspect((1, 1, 1), zoom=1.5)

# --- Rectangle parameters ---
rectLength = 16/9
rectWidth = 1

# --- Define rectangle centered at origin ---
x = np.array([np.linspace(-rectLength/2, rectLength/2, 1920)] * 1080)
y = np.rot90(np.array([np.linspace(-rectWidth/2, rectWidth/2, 1080)] * 1920))
z = np.zeros_like(x)

# --- Apply existing offset tilt (around x-axis) ---
offsetTheta = np.pi/6
x_tilt = x * np.cos(offsetTheta)
z_tilt = z + x * np.sin(-offsetTheta)

# --- Rotate around x-axis by theta_x (through origin) ---
theta_x = np.radians(-60)  # adjust this as desired
y_rot = y * np.cos(theta_x) - z_tilt * np.sin(theta_x)
z_rot = y * np.sin(theta_x) + z_tilt * np.cos(theta_x)

# --- Compute target position for rectangle center ---
x0 = np.cos(np.pi/3) * np.sin(np.pi/2 - np.pi/3)
y0 = np.sin(np.pi/3)
z0 = np.cos(np.pi/3) * np.cos(np.pi/2 - np.pi/3)

# --- Translate rectangle to target position ---
x_final = x_tilt + x0
y_final = y_rot + y0
z_final = z_rot + z0

# --- Plot positioned rectangle ---
ax.plot_surface(x_final, y_final, z_final, color='gray', rcount=1, ccount=1, alpha=1, zorder=0.0000000000001)

ax.set_xlim3d(-1, 2)
ax.set_ylim3d(-1, 2)
ax.set_zlim3d(-1, 2)

x, y, z = np.array([[-1,0,0],[0,-1,0],[0,0,-1]])
u, v, w = np.array([[1,0,0],[0,1,0],[0,0,1]])
ax.quiver(x,y,z,u,v,w,arrow_length_ratio=0.1, color="black", length=3)

ax.text(1.9, 0.1, 0, '$x$', size='x-large')
ax.text(0, 1.9, 0.1, '$y$', size='x-large')
ax.text(0, 0.1, 1.9, '$z$', size='x-large')

radius = 1
center_x, center_y, center_z = 0, 0, 0

theta = np.linspace(np.pi/3, np.pi/2, 100)
r = np.linspace(0, radius, 50)
theta, r = np.meshgrid(theta, r)
x_fill = center_x + r * np.cos(theta)
y_fill = np.full_like(x_fill, center_y)
z_fill = center_z + r * np.sin(theta)

# big azimuth
ax.plot_surface(x_fill, y_fill, z_fill, color='skyblue', alpha=0.5, zorder=3)

radius = 0.2
theta = np.linspace(np.pi/3, np.pi/2, 100)
r = np.linspace(0, radius, 50)
theta, r = np.meshgrid(theta, r)
x_fill = center_x + r * np.cos(theta)
y_fill = np.full_like(x_fill, center_y)
z_fill = center_z + r * np.sin(theta)

# small azimuth
ax.plot_surface(x_fill, y_fill, z_fill, color='black', alpha=1, zorder=3)

radius = 1
theta = np.linspace(0, np.pi/3, 100)
offsetTheta = np.pi/6

r = np.linspace(0, radius, 50)
theta, r = np.meshgrid(theta, r)
x_fill = center_x + r * np.cos(theta) * np.sin(offsetTheta)
y_fill = center_y + r * np.sin(theta)
z_fill = center_z + r * np.cos(theta) * np.cos(offsetTheta)

# big elevation
ax.plot_surface(x_fill, y_fill, z_fill, color='red', alpha=0.5, zorder=3)

radius = 0.2
theta = np.linspace(0, np.pi/3, 100)
offsetTheta = np.pi/6

r = np.linspace(0, radius, 50)
theta, r = np.meshgrid(theta, r)
x_fill = center_x + r * np.cos(theta) * np.sin(offsetTheta)
y_fill = center_y + r * np.sin(theta)
z_fill = center_z + r * np.cos(theta) * np.cos(offsetTheta)

# small elevation
ax.plot_surface(x_fill, y_fill, z_fill, color='black', alpha=1, zorder=3)

ax.text3D(0.1, 0, 0.3, "azimuth", (0, 0, 1))
ax.text3D(0.1, 0.2, 0.2, "elevation", (np.cos(np.pi/3) * np.sin(offsetTheta), np.cos(np.pi/3), np.cos(np.pi/3) * np.cos(offsetTheta)))


ax.set_axis_off()

plt.savefig('azimuthElevation.svg', bbox_inches='tight')

plt.show()
