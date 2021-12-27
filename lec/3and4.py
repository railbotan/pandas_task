import pandas as pd

works = pd.read_csv("./works.csv")

print(f"кол-во не NAN значений в столбце skills: {works['skills'].notna().sum()}")
print(f"заполненные скиллы:\n{works['skills'].dropna()}")
