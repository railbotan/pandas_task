import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

works = pd.read_csv('works.csv')

percentiles = np.linspace(.1, 1, 10)

#Перцентиль для мужчин
men_salary = works.query('gender == "Мужской"').quantile(percentiles)
fig, ax = plt.subplots()
ax.plot(percentiles, men_salary)
plt.xlabel('Перцентили')
plt.ylabel('Зарплата мужчин')
plt.show()

#Перцентиль для женщин
women_salary = works.query('gender == "Женский"').quantile(percentiles)
fig, ax = plt.subplots()
ax.plot(percentiles, women_salary)
plt.xlabel('Перцентили')
plt.ylabel('Зарплата женщин')
plt.show()