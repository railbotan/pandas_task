import pandas as pd

works = pd.read_csv('works.csv')

# Количество записей
print(works.shape[0])

# Количество мужчин
print('Количество мужчин ', works[works['gender'] == 'Мужской'].shape[0])

# Количество женщин
print('Количество женщин ', (works['gender'] == 'Женский').values.sum)
