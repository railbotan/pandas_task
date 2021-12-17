import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


works = pd.read_csv("works.csv")
head = works.head(5)
tail = works.tail(5)

skills_bool = works["skills"].str.lower().str.contains("python|питон") & works["skills"].notnull()
print(works[skills_bool]["salary"])
