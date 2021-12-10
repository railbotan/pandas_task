import pandas as pd

works = pd.read_csv("./works.csv")

works_notha = works['skills'].notna()
works_dropha = works['skills'].dropna().str.lower().str.contains('питон|python')

print(f"Заработная плата тех, кто владеет python (питон):\n",
      ', '.join(f"{i}" for i in works[works_notha][works_dropha]['salary'].values))