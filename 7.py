import numpy as np
import pandas as pd
import matplotlib.pyplot as mp

works = pd.read_csv("works.csv")
men_salary = works.query("gender == 'Мужской'").groupby("educationType").agg("mean").reset_index()
women_salary = works.query("gender == 'Женский'").groupby("educationType").agg("mean").reset_index()

educationTypes = men_salary["educationType"].values
men_salaries = men_salary["salary"].values
women_salary = women_salary["salary"].values

index = np.arange(len(educationTypes))

bw = 0.4
mp.bar(index-bw/2, men_salaries, bw, color="b", label="Средняя зарплата мужчин")
mp.bar(index+bw/2, women_salary, bw, color="r", label="Средняя зарплата женщин")
mp.xticks(index, educationTypes, rotation=45)
mp.legend()
mp.show()