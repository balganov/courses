import matplotlib.pyplot as plt
import numpy as np

data = {"city1":1,"city2":2,"city3":3,"city4":4}

f, ax = plt.subplots(2,2)

ax[0].pie(data.values(), labels=data.keys())
ax[1].pie(data.values(), labels=data.keys())
ax[2].pie(data.values(), labels=data.keys())
ax[3].pie(data.values(), labels=data.keys())


plt.savefig("test.png")
