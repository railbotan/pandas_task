import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

works = pd.read_csv("./works.csv")

m = works[works['gender'] == 'Мужской']['salary']
fm = works[works['gender'] == 'Женский']['salary']
pr = [i / 10 for i in range(1, 11)]

ax = plt.subplots()[1]
print("Мужчины:\n")
ax.plot(m.quantile(pr))
plt.show()
print("Женщины:\n")
ax.plot(fm.quantile(pr))
plt.show()
