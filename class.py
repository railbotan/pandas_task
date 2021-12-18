import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('works.csv')

# 1
print(len(data.index))
print(data.shape[0])
print(data.info())

# 2
# print((data['gender']=='Мужской').sum(), (data['gender']=='Женский').sum())
print(data.gender.value_counts())

# 3
print(data.info())
print(data.skills.notna().sum())
print(data.skills.count())

# 4
print(data[data.skills.notna()]['skills'])
print(data.skills.dropna())

# 5
new_data = data[data.skills.notna()]
print(new_data[new_data.skills.str.lower().str.contains('python|питон')].salary)

# 6
index = data.skills.str.lower().str.contains('python|питон')
mask = index.notna()
print(data[mask & index].salary)

# 7
data.query("gender == 'Мужской' and educationType == 'Высшее'").hist(bins=100, alpha=0.5)
plt.show()

data.query("gender == 'Женский' and educationType == 'Высшее'").hist(bins=100, alpha=0.5)
plt.show()