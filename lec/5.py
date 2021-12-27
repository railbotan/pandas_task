import pandas as pd

works = pd.read_csv("./works.csv")

nNa = works['skills'].notna()
df = works['skills'].dropna().str.lower().str.contains('питон|python')

print(f"зарплата тех, у кого в скиллах есть python (питон):\n",
      ', '.join(f"{i}" for i in works[nNa][df]['salary'].values))
