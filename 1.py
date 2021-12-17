import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('works.csv')
rows_count = df.shape[0]
print("Всего записей:", rows_count)