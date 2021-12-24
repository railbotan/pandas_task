import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

works = pd.read_csv('works.csv',encoding='utf-8')
count_of_rows = works.shape[0]
print((works['gender'] == 'Мужской').sum())
print((works['gender'] == 'Женский').sum())
print(works['skills'].notna().sum())
print(works.info())
print(works['skills'].count())
print(works[works['skills'].notna()]['skills'])
print(works['skills'].dropna())
zarp = works['skills'].str.lower().str.contains("python|питон")
p1 = works['skills'].notna().sum()

print(works[zarp & p1]['salary'])
print(works.describe())

a = 20000
b = 'Высшее'
work_query = works.query('salary == @a and educationType == @b')
print(work_query[['salary','educationType']])
percentiles = np.linspace(.1, 1, 10)
men_salary = works.query("gender == 'Мужской'").quantile(percentiles)
women_salary = works[works.gender == 'Женский']['salary'].quantile(percentiles)
plt.plot(men_salary, color='blue')
plt.plot(women_salary, color='red')
plt.xlabel('Перцентили')
plt.ylabel('Зарплата')
plt.show()

men_salary = works.query("gender == 'Мужской'").groupby('educationType').agg('mean')['salary'].values
women_salary = works.query("gender == 'Женский'").groupby('educationType').agg('mean')['salary'].values

educationType = set(works['educationType'].dropna().values)

index = np.arange(len(educationType))
width = 0.3
plt.bar(index - width / 2, men_salary, width, color='blue', label='Средняя зарплата мужчин')
plt.bar(index + width / 2, women_salary, width, color='red', label='Средняя зарплата женщин')
plt.xticks(index, educationType)
plt.legend()
plt.show()

