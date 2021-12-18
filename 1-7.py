import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

works = pd.read_csv('works.csv')
# 1
print('общее количество записей в датасете:', works.shape[0])  # 32683
# 2
print('Количество мужчин:', works[works['gender'] == 'Мужской'].shape[0])  # 13386
print('Количество женщин:', (works['gender'] == 'Женский').sum())  # 17910
# 3
print('Количество значений в столбце skills не NAN:', works['skills'].notna().values.sum())  # 8972
# 4
print('Все заполненные скиллы:\n', works['skills'].dropna())
# 5
skills_base = works.skills.str.lower().str.contains('python|питон').dropna()
print('Зарплата у тех, у кого в скиллах есть Python(Питон):\n', works[works.skills.notna()][skills_base]['salary'])
# 6
percentiles = np.linspace(.1, 1, 10)
m_salary = works[works.gender == 'Мужской']['salary'].quantile(percentiles)
w_salary = works[works.gender == 'Женский']['salary'].quantile(percentiles)
plt.plot(m_salary, color='blue')
plt.plot(w_salary, color='red')
plt.xlabel('Перцентили')
plt.ylabel('Зарплата')
plt.show()
# 7
men_salary = works.query('gender == "Мужской"').groupby('educationType').agg('mean').reset_index()
women_salary = works.query('gender == "Женский"').groupby('educationType').agg('mean').reset_index()
educationType = men_salary['educationType'].values
men_salary = men_salary['salary'].values
women_salary = women_salary['salary'].values
index = np.arange(len(educationType))
wd = 0.1
plt.bar(index - wd / 2, men_salary, wd, color='blue', label='Средняя зарплата мужчин')
plt.bar(index + wd / 2, women_salary, wd, color='red', label='Средняя зарплата женщин')
plt.xticks(index, educationType)
plt.legend()
plt.show()
