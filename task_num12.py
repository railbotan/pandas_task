import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

works = pd.read_csv('works.csv')

# Количество записей
print(works.shape[0])

# Количество мужчин
print('Количество мужчин ', works[works['gender'] == 'Мужской'].shape[0])

# Количество женщин
print('Количество женщин ', (works['gender'] == 'Женский').values.sum)
