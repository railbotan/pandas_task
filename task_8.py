import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

works = pd.read_csv('works.csv')
#очистить и визуализировать данные по профессии инженер и должности менеджер

print(works[works['qualification'] == 'Менеджер'])