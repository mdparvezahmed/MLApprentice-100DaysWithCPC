import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random



head_tails = [0,0]

for _ in range(200):
    head_tails[random.randint(0,1)]+=1
    plt.bar(["Heads","Tails"], head_tails, color=["red","blue"])
    plt.pause(0.001)
plt.show()



#==========3d view================


# ax = plt.axes(projection="3d")

# x = np.arange(-5,5, 0.1)
# y = np.arange(-5, 5, 0.1)
# X, Y = np.meshgrid(x, y)
# Z = np.sin(X) * np.cos(Y)


# surf = ax.plot_surface(X, Y, Z, cmap="Spectral")

# ax.set_title("3D plot")
# # ax.view_init(azim=0, elev=90)
# plt.show()