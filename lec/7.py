import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

works = pd.read_csv("./works.csv")


genders = set(works.dropna()["gender"])
educations = set(works.dropna()["educationType"])

dataToPlot = works.groupby(['gender', 'educationType'])['salary'].mean()
dataToPlot.plot.bar()
