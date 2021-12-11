import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv('works.csv')

#Введение

#print(file.head(10))
#print(file.tail(10))
#print(file.info())
#print(file.describe())
#print(file['gender'])
#print(file['gender'].describe())
#print(file.count())

#1

#print(len(file.index))

#2

#print(file[file['gender'] == 'Мужской'].shape[0])
#print((file['gender'] == 'Женский').values.sum())
#print(file['gender'].value_counts())

#3

#print(file['skills'].notna().values.sum())
#print(file['skills'].notnull().values.sum())
#print(file['skills'].dropna().shape[0])

#4

#print(file[file['skills'].notna()]['skills'])
#print(file['skills'].dropna())
#print(file.query("skills == skills")["skills"])
#a = 25000
#b = 'Женский'
#print(file.query('salary == @a and gender == @b'))

#5

#a = file.skills.dropna().str.lower().str.contains('python|питон')
#print(file[file.skills.notna()][a]['salary'])

#6

#per = np.linspace(.1, 1, 10)
#men = file.query('gender == "Мужской"').quantile(per)
#women = file.query('gender == "Женский"').quantile(per)

#fig1, ax = plt.subplots()
#ax.plot(per, men)
#plt.xlabel("Перцентили")
#plt.ylabel("Зарплата мужчин")
#plt.show()

#fig2, ax = plt.subplots()
#ax.plot(per, women)
#plt.xlabel("Перцентили")
#plt.ylabel("Зарплата женщин")
#plt.show()

#7 Нужно вставить эти команды в JupyterNotebook

#file.query("gender == 'Мужской' and educationType == 'Высшее'").hist(bins=100, alpha=0.5)
#file.query("gender == 'Мужской' and educationType == 'Незаконченное высшее'").hist(bins=100, alpha=0.5)
#file.query("gender == 'Мужской' and educationType == 'Среднее профессиональное'").hist(bins=100, alpha=0.5)
#file.query("gender == 'Мужской' and educationType == 'Среднее'").hist(bins=100, alpha=0.5)

#file.query("gender == 'Женский' and educationType == 'Высшее'").hist(bins=100, alpha=0.5)
#file.query("gender == 'Женский' and educationType == 'Незаконченное высшее'").hist(bins=100, alpha=0.5)
#file.query("gender == 'Женский' and educationType == 'Среднее профессиональное'").hist(bins=100, alpha=0.5)
#file.query("gender == 'Женский' and educationType == 'Среднее'").hist(bins=100, alpha=0.5)