import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x=np.linspace(-5,5,100)
y=np.sin(x)
plt.figure(figsize=(8,6))
plt.plot(x,y,label="sin(x)",color='b')
plt.title("2D plot of sin(x)")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.grid(True)
plt.show()

x_3d=np.linspace(-5,5,100)
y_3d=np.linspace(-5,5,100)
x_3d,y_3d=np.meshgrid(x_3d,y_3d)
z_3d=np.sin(np.sqrt(x_3d**2+y_3d**2))
fig=plt.figure(figsize=(10,7))
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(x_3d,y_3d,z_3d,cmap='viridis')
ax.set_title("3D Plot of Sin(sqrt(x^2+y^2))")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.set_zlabel("Z-Axis")
plt.show()
