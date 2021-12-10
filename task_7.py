import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

works = pd.read_csv('works.csv')

men_salary = works.query('gender == "Мужской"').groupby("educationType").agg("mean").reset_index()
men = men_salary['salary'].values
women_salary = works.query('gender == "Женский"').groupby("educationType").agg("mean").reset_index()
women = women_salary['salary'].values

types = men_salary["educationType"].values
id = np.arange(len(types))

plt.bar(id - 0.2, men, 0.4, color="g", label = "Средняя зарплата мужчин")
plt.bar(id + 0.2, women, 0.4, color="y", label = "Средняя зарплата женщин")
plt.xticks(id, types, rotation=45)
plt.legend()
plt.show()