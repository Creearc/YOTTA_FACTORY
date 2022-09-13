import matplotlib.pyplot as plt
import numpy as np

from word3 import data

# prepare some coordinates
x, y, z = np.indices((80, 80, 80))

# draw cuboids in the top left and bottom right corners, and a link between
# them

voxels = []
voxelarray = None
for element in data:
    voxels.append((x == element['x']) & (y == element['y']) & (z == element['z']))
    if voxelarray is None:
        voxelarray = voxels[0]
    else:
        voxelarray = voxelarray | voxels[-1]


# set the colors of each object
colors = np.empty(voxelarray.shape, dtype=object)
for element in voxels:
    colors[element] = 'blue'

# and plot everything
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

plt.show()
