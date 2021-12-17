import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('works.csv')
def get_rows_with_gender(df: pd.DataFrame, gender: str) -> pd.DataFrame:
    return df[df["gender"] == gender]
females = get_rows_with_gender(df, "Женский")
males = get_rows_with_gender(df, "Мужской")
skills = df[df["skills"].notna()]
print("Все заполненные скиллы:\n", skills["skills"])
