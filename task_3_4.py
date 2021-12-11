import pandas as pd

data = pd.read_csv('works.csv')

print('Количество skills не NaN ', data.skills.notna().values.sum())
print(data[data.skills.notna()]['skills'])

salary = 20000
group = 'Женский'

print(data.query('salary == @salary and gender == @group'))