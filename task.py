import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

works = pd.read_csv('works.csv')

# Количество записей в датасете

# countRecords = works.shape
# print(countRecords)
# countRecords1 = len(works.index)
# print(countRecords1)


# Количество мужчин и женщин

# genderMale = works[works['gender'] == 'Мужской'].shape[0]
# print(genderMale)
# genderFemale = (works['gender'] == 'Женский').values.sum()
# print(genderFemale)
# genders = works['gender'].value_counts()
# print(genders)


# Узнать сколько значений в столбце skills не NAN;

# s = works['skills'].notnull().values.sum()
# print(s)
# s1 = works['skills'].dropna().shape[0]
# print(s1)


# Получить все заполненные скиллы;

# s = works['skills'].dropna()
# print(s)
# s1 = works.query("skills == skills")["skills"]
# print(s1)

# a = 10000
# b = 'Женский'
# print(works.query("salary == @a and gender == @b"))


# Вывести зарплату только у тех, у которых в скиллах есть Python (Питон);

# df = works.skills.dropna().str.lower().str.contains('python|питон')
# print(works[works.skills.notna()][df]['salary'])


# Построить перцентили по заработной плате у мужчин и женщин;

# percentiles = np.linspace(.1, 1, 10)
# men_salary = works.query("gender == 'Мужской'").quantile(percentiles)
# women_salary = works.query("gender == 'Женский'").quantile(percentiles)
#
# fig, ax1 = plt.subplots()
# ax1.plot(percentiles, men_salary)
# plt.xlabel("Перцентили")
# plt.ylabel("Зарплата мужчин")
#
# fig, ax2 = plt.subplots()
# ax2.plot(percentiles, women_salary)
# plt.xlabel("Перцентили")
# plt.ylabel("Зарплата женщин")
# plt.show()


# Построить графики распределения по заработной плате мужчин и женщин в зависимости от высшего образования;

men_salary = works.query("gender == 'Мужской'").groupby("educationType").agg("mean").reset_index()
women_salary = works.query("gender == 'Женский'").groupby("educationType").agg("mean").reset_index()
print(men_salary)
print(women_salary)

educationTypes = men_salary["educationType"].values
men_salaries = men_salary["salary"].values
women_salaries = women_salary["salary"].values
index = np.arange(len(educationTypes))

bw = 0.4
plt.bar(index-bw/2, men_salaries, bw, color="b", label="Средняя зарплата мужчин")
plt.bar(index+bw/2, women_salaries, bw, color="r", label="Средняя зарплата женщин")
plt.xticks(index, educationTypes, rotation=45)
plt.legend()
plt.show()

# Надо прочитать как установить модуль юпитера
works.query("gender == 'Мужской' and educationType == 'Высшее'").hist(bins=100, alpha=0.5)
works.query("gender == 'Женский' and educationType == 'Высшее'").hist(bins=100, alpha=0.5)

works.query("gender == 'Мужской' and educationType == 'Незаконченное высшее'").hist(bins=100, alpha=0.5)
works.query("gender == 'Женский' and educationType == 'Незаконченное высшее'").hist(bins=100, alpha=0.5)

works.query("gender == 'Мужской' and educationType == 'Среднее'").hist(bins=100, alpha=0.5)
works.query("gender == 'Женский' and educationType == 'Среднее'").hist(bins=100, alpha=0.5)

works.query("gender == 'Мужской' and educationType == 'Среднее профессиональное'").hist(bins=100, alpha=0.5)
works.query("gender == 'Женский' and educationType == 'Среднее профессиональное'").hist(bins=100, alpha=0.5)