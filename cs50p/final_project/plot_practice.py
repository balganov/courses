import matplotlib.pyplot as plt
import matplotlib as mpl

import numpy as np

data = {"city1":1,"city2":2,"city3":3,"city4":4}

f, ax = plt.subplots(2,2)
cmap = mpl.colormaps['viridis']
colors = cmap(range(len(data)))
print(colors)

ax[0,0].set_title('Pie Chart 1')
ax[0,0].pie(data.values(), labels=data.keys(),colors=colors)
ax[0,1].set_title('Pie Chart 2')
ax[0,1].pie(data.values(), labels=data.keys(),colors=colors)
ax[1,0].set_title('Pie Chart 3')
ax[1,0].pie(data.values(), labels=data.keys())
ax[1,1].set_title('Pie Chart 4')
ax[1,1].pie(data.values(), labels=data.keys())


plt.savefig("test.png")
