import pandas as pd

works = pd.read_csv("./works.csv")

print(f"кол-во записей: {len(works)}\n"
      f"кол-во мужчин: {len(works[works['gender'] == 'Мужской'])}\n"
      f"кол-во женщин: {len(works[works['gender'] == 'Женский'])}")
