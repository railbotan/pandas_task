import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('works.csv')
def get_rows_with_gender(df: pd.DataFrame, gender: str) -> pd.DataFrame:
    return df[df["gender"] == gender]
females = get_rows_with_gender(df, "Женский")
males = get_rows_with_gender(df, "Мужской")
no_none_skills_count = df["skills"].count()

print("Значений в столбце skills не NAN:", no_none_skills_count)