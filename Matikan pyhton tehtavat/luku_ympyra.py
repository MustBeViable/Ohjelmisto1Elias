
from matplotlib import pyplot as plt, patches
import numpy as np


fig = plt.figure()
ax = fig.subplots(1,1)

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')




pii=np.pi
pist_xy=np.array([pii, pii, pii, pii, 2*pii, 5*pii, pii, 3*pii])
nim=np.array([6, 4, 3, 2, 3, 6, 1, 2])
varit=np.array(['red', 'green', 'blue', 'orange', 'brown', 'black', 'purple', 'pink'])

text=['30', '45', '60', '90',
          '120', '150', '180', '270']

x = np.cos(pist_xy/nim)
y = np.sin(pist_xy/nim)

plt.scatter(x, y, color=varit, marker='X')

for i in range(len(pist_xy)):
    plt.annotate(text[i],
             xy=(np.cos(pist_xy[i]/nim[i]), np.sin(pist_xy[i]/nim[i])), xycoords='data',
             xytext=(+30, +5), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

plt.show()