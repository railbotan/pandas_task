import pandas as pd

works = pd.read_csv('works.csv')

print('Количество skills не NAN ', works.skills.notna().values.sum())

print(works[works.skills.notna()]['skills'])

s = 20000
g = 'Женский'
print(works.query('salary == @s and gender == @g'))
