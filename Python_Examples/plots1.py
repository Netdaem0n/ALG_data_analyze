import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Assuming df is your DataFrame and you want to plot columns 'A', 'B', 'C'
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['A'], df['B'], df['C'])

ax.set_xlabel('A')
ax.set_ylabel('B')
ax.set_zlabel('C')

plt.show()