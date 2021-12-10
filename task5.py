import pandas as pd

works = pd.read_csv('works.csv')

df = works.skills.dropna().str.lower().str.contains('python|питон')

print('Зарплата тех, у которых в скиллах есть Python (Питон)\n', works[works.skills.notna()][df]['salary'])
