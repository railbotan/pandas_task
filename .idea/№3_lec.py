import pandas as pd

works = pd.read_csv("./works.csv")

print(works['skills'].notna().values.sum())
print(works['skills'].notnull().values.sum())
print(works['skills'].dropna().shape[0])