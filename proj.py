import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

works = pd.read_csv("works.csv")
print(works['skills'].str.lower().str.contains('python|питон'))

works = pd.read_csv("works.csv")
head = works.head(5)
print(head)

tail = works.tail(5)
print(tail)
print(works.shape[0])
print(len(works.index))

print(works[works['gender'] == 'Мужской'].shape[0])
print((works['gender'] == 'Женский').sum())
print(works['gender'].value_counts())

print(works['skills'].notnull().sum())
print(works.info())
print(works['skills'].count())

print(works[works['skills'].notnull()]['skills'])
print(works['skills'].dropna())
print(works.query("skills == skills")["skills"])
print(works.query("salary == 15000"))
edu = 'Высшее'
gen = 'Женский'
print(works.query("educationType == @edu and gender == @gen")[['salary', 'educationType','gender']])

mask = works["skills"].str.lower().str.contains("python|питон") & works["skills"].notnull()
print(works[mask]["salary"])

percentiles = np.linspace(.1, 1, 10)

gen = "Мужской"
men_salary = works.query('gender == @gen').quantile(percentiles)
fig, ax = plt.subplots()
ax.plot(percentiles, men_salary)
plt.xlabel('Перцентили')
plt.ylabel('Зарплата мужчин')
plt.show()

gen = "Женский"
women_salary = works.query('gender == @gen').quantile(percentiles)
fig, ax = plt.subplots()
ax.plot(percentiles, women_salary)
plt.xlabel('Перцентили')
plt.ylabel('Зарплата женщин')
plt.show()

gen = "Мужской"
men_salary = works.query('gender == @gen').groupby("educationType").agg("mean").reset_index()
men = men_salary['salary'].values
gen = "Женский"
women_salary = works.query('gender == @gen').groupby("educationType").agg("mean").reset_index()
women = women_salary['salary'].values

types = men_salary["educationType"].values
id = np.arange(len(types))

plt.bar(id - 0.2, men, 0.4, color="g", label = "Средняя зарплата мужчин")
plt.bar(id + 0.2, women, 0.4, color="y", label = "Средняя зарплата женщин")
plt.xticks(id, types, rotation=45)
plt.legend()
plt.show()