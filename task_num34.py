import pandas as pd

works = pd.read_csv('works.csv')

print('Кол-во skills не NAN', works.skills.notna().values.sum())

print(works[works.skills.notna()]['skills'])

j = 20000
d = 'Женский'
print(works.query('salary == @j and gender == @d'))
