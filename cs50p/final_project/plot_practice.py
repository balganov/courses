import matplotlib.pyplot as plt
import matplotlib as mpl

import numpy as np

data = [
        {'Almaty': 141, 'Astana': 53, 'Temirtau': 2, 'Shymkent': 2,'Atyrau': 1},
        {'IT, System Integration, Internet': 67, 'Financial Sector': 59, 'Retail': 26, 'Telecommunications, Communications': 25, 'Business Services': 24},
        {'Between 3 and 6 years': 100, 'Between 1 and 3 years': 72, 'No experience': 24, 'More than 6 years': 13},
        {'BI analyst, data analyst': 118, 'Data scientist': 71, 'Product analyst': 20},
        {"At the employer's location": 99, 'Hybrid': 53, 'Remote': 49, 'Travel': 1},
        {}
]

r = 2
c = 3
n = 0
f, ax = plt.subplots(r,c, figsize=(20,10))
colors = plt.get_cmap('viridis')(np.linspace(0.9, 0.4, len(data)))

print(colors)


ax[0,0].set_title("Professional roles")
ax[0,0].pie(data[3].values(), labels=data[3].keys(), colors=colors, autopct='%.2f%%')
ax[0,1].pie(data[1].values(), labels=data[1].keys(), colors=colors, autopct='%.2f%%')
ax[0,2].pie(data[2].values(), labels=data[2].keys(), colors=colors, autopct='%.2f%%')

ax[1,0].bar(data[0].keys(), data[0].values(), color=colors)

ax[1,2].bar(data[4].keys(), data[4].values(), color=colors)

plt.tight_layout()
plt.savefig("test.png")
