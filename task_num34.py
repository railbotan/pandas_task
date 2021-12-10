import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

works = pd.read_csv('works.csv')

print('Кол-во skills не NAN', works.skills.notna().values.sum())

print(works[works.skills.notna()]['skills'])

j = 20000
d = 'Женский'
print(works.query('salary == @j and gender == @d'))