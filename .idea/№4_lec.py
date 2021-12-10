import pandas as pd

works = pd.read_csv("./works.csv")

a = 25000
b = 'Женский'

print(works[works['skills'].notna()]['skills'])
print(works['skills'].dropna())
print(works.query("skills == skills")["skills"])
print(file.query('salary == @a and gender == @b'))