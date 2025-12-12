import matplotlib.pyplot as plt
import numpy as np

data = {"city1":1,"city2":2,"city3":3,"city4":4}

f, ax = plt.subplots()

ax.pie(data.values(), labels=data.keys())
#plt.savefig("test.png")
