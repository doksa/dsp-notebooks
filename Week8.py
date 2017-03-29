import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib import cm

# Illustration of the "landscape" defined by poles and zeros, and the
# corresponding magnitude response


zeros = np.array([0.7, 0.99])
poles = np.array([-2 + 2*1j, -2 - 2*1j, .9 - .3*1j])

x_max = 4
n_x = 400

x = np.linspace(-x_max, x_max, n_x)
X, Y = np.meshgrid(x, x)

H = np.ones(X.shape, dtype=np.complex128)
t = np.linspace(0, 2*np.pi, 256)
circz = np.ones(t.shape, dtype=np.complex128)

for zero in zeros:
    H *= X + 1j*Y - zero
    circz *= np.cos(t) + 1j*np.sin(t) - zero
    
for pole in poles:
    H /= X + 1j*Y - pole
    circz /= np.cos(t) + 1j*np.sin(t) - pole


from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 5))
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(X, Y, np.log(np.abs(H)), cmap=cm.coolwarm, linewidth=0, antialiased=True)
ax.plot(np.cos(t), np.sin(t), np.log(np.abs(circz)) + 0.1, 'g', linewidth=2)
ax.plot(np.cos(t), np.sin(t), -10, color=[.5,.5,.5], linewidth=2)
ax.set_zlim3d(-10, 4)

ax = fig.add_subplot(122)
ax.plot(t, np.log(np.abs(circz)))


plt.show()
