import pandas as pd

works = pd.read_csv('works.csv')
# task 1
print('Общее количество записей в датасете:', works.shape[0])
# task 2
print('Количество мужчин:', works[works['gender'] == 'Мужской'].shape[0])
print('Количество женщин:', (works['gender'] == 'Женский').sum())
# task 3
print('Количество значений в столбце skills не NAN:', works['skills'].notna().values.sum())
# task 4
print('Все заполненные скиллы:\n', works['skills'].dropna())
# task 5
skills_base = works.skills.str.lower().str.contains('python|питон').dropna()
print('Зарплата у тех, у кого в скиллах есть Python (Питон):\n', works[works.skills.notna()][skills_base]['salary'])

