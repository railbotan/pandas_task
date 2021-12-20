import pandas as pd

works = pd.read_csv('works.csv')

df = (works.skills.dropna().str.lower().str.contains('python|питон'))

print(works[works.skills.notna()][df]['salary'])
