import numpy as np
import pandas as pd

works = pd.read_csv("works.csv").dropna()

print("task 1")
print(f"кол-во записей: {len(works)}\n")

print("task 2")
print(f"кол-во мужчин: {len(works[works['gender'] == 'Мужской'])}\n"
      f"кол-во женщин: {len(works[works['gender'] == 'Женский'])}")

print("task 3")
print("всего скилов:", works["skills"].count())
print("не NAN значений в скилах:", works["skills"].notnull().sum())
print(works[works["skills"].notnull()]["skills"])
print("заполненные скилы\n", works['skills'].dropna())

print("task 4")
edu = 'Высшее'
gen = 'Мужской'
print(works.query("educationType == @edu and gender == @gen")[['salary', "educationType", "gender"]])

print("task 5")
mask = works["skills"].notnull() & works["skills"].str.lower().str.contains("python|питон")
print("зарплата тех, у кого в скилах есть питон:\n", works[mask]["salary"])

print("task 6")
m = works[works['gender'] == 'Мужской']['salary'].values
fm = works[works['gender'] == 'Женский']['salary'].values
m_pcs = np.percentile(m, [x / 100.0 for x in range(100)])
print(m_pcs[50])
