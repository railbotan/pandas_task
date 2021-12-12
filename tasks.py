import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


works = pd.read_csv("works.csv")
head = works.head(5)
tail = works.tail(5)


# Задание 1
print(len(works.index))

# Задание 2
print(works["gender"].value_counts())

# Задание 3
print(works["skills"].count())

# Задание 4
print(works["skills"].dropna())

# Задание 5
skills_bool = works["skills"].str.lower().str.contains("python|питон") & works["skills"].notnull()
print(works[skills_bool]["salary"])

# Задание 6
person = np.linspace(.1, 1, 10)
men = works.query('gender == "Мужской"').quantile(person)
women = works.query('gender == "Женский"').quantile(person)
print(men)
print(women)
