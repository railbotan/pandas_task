import pandas as pd

data = pd.read_csv('works.csv')

print('Количество всех записей: ', data.shape[0])
print('Количество мужчин: ', data[data['gender'] == 'Мужской'].shape[0])
print('Количество женщин: ', (data['gender'] == 'Женский').values.sum())