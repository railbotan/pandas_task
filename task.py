import numpy as np
import pandas as pd
import matplotlib.pyplot as mp

works = pd.read_csv("works.csv")

# 1
print("Общее количество записей:", works.shape[0])

# 2
print("Количество мужчин:", works[works["gender"] == "Мужской"].shape[0])
print("Количество женщин:", (works["gender"] == "Женский").sum())

# 3
print("Количество не NaN значений", works["skills"].count())

# 4
print("Все заполненные скиллы\n", works['skills'].dropna())

# 5
skills_bool = works['skills'].str.lower().str.contains('python | питон') & works['skills'].notnull()
print("Зарплата тех, у кого в скиллах есть Python (Питон)\n", works[skills_bool]['salary'])

# 6
salary_p = np.linspace(0.1, 1, 10)
w = works[works.gender == "Женский"]['salary'].quantile(salary_p)
m = works[works.gender == "Мужской"]['salary'].quantile(salary_p)

mp.plot(m, salary_p, color='blue')
mp.plot(w, salary_p, color='r')
mp.xlabel('salary')
mp.ylabel('quantile')
mp.show()

# 7
men_salary = works.query("gender == 'Мужской'").groupby("educationType").agg("mean").reset_index()
women_salary = works.query("gender == 'Женский'").groupby("educationType").agg("mean").reset_index()

educationTypes = men_salary["educationType"].values
men_salaries = men_salary["salary"].values
women_salary = women_salary["salary"].values

index = np.arange(len(educationTypes))

bw = 0.4
mp.bar(index-bw/2, men_salaries, bw, color="b", label="Средняя зарплата мужчин")
mp.bar(index+bw/2, women_salary, bw, color="r", label="Средняя зарплата женщин")
mp.xticks(index, educationTypes, rotation=45)
mp.legend()
mp.show()