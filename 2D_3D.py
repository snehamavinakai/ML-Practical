import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample Data
x = np.linspace(-5, 5, 100)  # X values
y = np.linspace(-5, 5, 100)  # Y values
X, Y = np.meshgrid(x, y)  # Create a meshgrid

# Calculate Z values for a wave-like pattern (Sine wave)
Z_wave = np.sin(X)  # 2D sine wave for the contour plot

# Create a figure for 2D and 3D plots
plt.figure(figsize=(12, 6))

# 2D Wave Plot (contour plot)
plt.subplot(1, 2, 1)
plt.contourf(X, Y, Z_wave, cmap='viridis')  # Contour plot for the wave
plt.title('2D Wave (Sine Wave)')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar()

# 3D plot (Surface plot for sine wave)
Z_3d_wave = np.sin(np.sqrt(X**2 + Y**2))  # 3D sine wave pattern

ax = plt.subplot(1, 2, 2, projection='3d')
ax.plot_surface(X, Y, Z_3d_wave, cmap='plasma')
ax.set_title('3D Surface Plot (Wave)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Display the plots
plt.tight_layout()
plt.show()
