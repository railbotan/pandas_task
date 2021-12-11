import numpy as np
import pandas as pd
import matplotlib as plt

# 1 task
print(works.info())
print(works.shape[0])
print(len(works.index))

# 2 task
print(works[works["gender"] == "Мужской"].shape[0])
print((works["gender"] == "Женский").sum())
print(works["gender"].value_counts())

# 3 task
print(works["skills"].notnull().sum())
print(works.info())
print(works["skills"].count())
print(works[works["skills"].notnull()]["skills"])
print(works['skills'].dropna())
print(works.query("skills == skills")["skills"])
print(works.query('salary == 15000'))

# 4 task
edu = 'Высшее'
gen = 'Мужской'
print(works.query("educationType == @edu and gender == @gen")[['salary', "educationType", "gender"]])

# 5 task
mask = works["skills"].str.lower().str.contains("python|питон") & works["skills"].notnull()
print(works[mask]["salary"])

# 6 task
works = pd.read_csv("./works.csv")
person = np.linspace(.1, 1, 10)
men = works.query('gender == "Мужской"').quantile(person)
women = works.query('gender == "Женский"').quantile(person)
print(men)
print(women)
