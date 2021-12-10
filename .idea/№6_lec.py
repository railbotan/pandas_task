import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

works = pd.read_csv("./works.csv")

person = np.linspace(.1, 1, 10)
men = works.query('gender == "Мужской"').quantile(person)
women = works.query('gender == "Женский"').quantile(person)
print(men)
print(women)