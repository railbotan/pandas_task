import pandas as pd

works = pd.read_csv("./works.csv")

print(f"количество мужчин: {len(works[works['gender'] == 'Мужской'])}\n"
      f"количество женщин: {len(works[works['gender'] == 'Женский'])}")