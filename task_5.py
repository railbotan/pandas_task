import pandas as pd

data = pd.read_csv('works.csv')
df = data.skills.dropna().str.lower().str.contains('python|питон')

print('Зарплата людей, у которых в skills есть Python\n', data[data.skills.notna()][df]['salary'])

