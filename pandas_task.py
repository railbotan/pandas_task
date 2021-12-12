import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

works = pd.read_csv("works.csv")
count = works.shape[0]
# задание №1
print("Всего записей - " + str(count))
women = works[works["gender"] == "Женский"].shape[0]
man = works[works["gender"] == "Мужской"].shape[0]
# задание №2
print("Мужчин - " + str(man) + ", Женщин - " + str(women))
nan_count = works[works["skills"].notna()].shape[0]
# задание №3
print("Кол-во не NaN - " + str(nan_count))
# задание №4
print(works[works["skills"].notna()]["skills"])
# задание №5
python_skills = works.skills.dropna().str.lower().str.contains("python|питон")
print(works[works.skills.notna()][python_skills]["salary"])
# задание №6
perc = np.linspace(.1, 1, 10)
men_salary = works.query("gender == 'Мужской'").quantile(perc)
women_salary = works.query("gender == 'Женский'").quantile(perc)
plt.plot(men_salary)
plt.plot(women_salary)
plt.show()

