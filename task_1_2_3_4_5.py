import pandas as pd

works = pd.read_csv('works.csv')

#Задача 1
print('Общее количество записей в датасете:', len(works.index))
print()

#Задача 2
print('Количество мужчин в датасете:', works[works['gender'] == 'Мужской'].shape[0])
print('Количество женщин в датасете:', works[works['gender'] == 'Женский'].shape[0])
print()

#Задача 3
print(works['skills'].notnull().values.sum(), 'значений в столбце skills не NAN')
print()

#Задача 4
print('Все заполненные скиллы:')
print(works['skills'].dropna())
print()

#Задача 5
print('Зарплата тех, у кого в скиллах есть Python (Питон):')
ans = works.skills.dropna().str.lower().str.contains('(python|питон)')
print(works[works.skills.notna()][ans]['salary'])