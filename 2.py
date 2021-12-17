import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('works.csv')
def get_rows_with_gender(df: pd.DataFrame, gender: str) -> pd.DataFrame:
    return df[df["gender"] == gender]
females = get_rows_with_gender(df, "Женский")
males = get_rows_with_gender(df, "Мужской")
print("Всего женщин:", females.shape[0])
print("Всего мужчин:", males.shape[0])