import pandas as pd

works = pd.read_csv('works.csv')

print('Количество записей ', works.shape[0])

print('Количество мужчин ', works[works['gender'] == 'Мужской'].shape[0])

print('Количество женщин ', (works['gender'] == 'Женский').values.sum())
