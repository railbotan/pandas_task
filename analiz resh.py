import numpy as np
import pandas as pd
import matplotlib as plt

works = pd.read_csv('works.csv', encoding='utf-8')

print(f"общее количество записей в датасете = { works.shape[0] }")

