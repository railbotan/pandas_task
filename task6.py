import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

works = pd.read_csv("./works.csv")

percentiles = np.linspace(.1, 1, 10)

men_salary = works.query('gender == "Мужской"').quantile(percentiles)
women_salary = works.query('gender == "Женский"').quantile(percentiles)

fig1, ax = plt.subplots()
ax.plot(percentiles, men_salary)
plt.xlabel("Перцентили")
plt.ylabel("Зарплата мужчин")

plt.show()

fig2, ax = plt.subplots()
ax.plot(percentiles, men_salary)
plt.xlabel("Перцентили")
plt.ylabel("Зарплата женщин")

plt.show()
