import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

works = pd.read_csv('works.csv')

df = (works.skills.dropna().str.lower().str.contains('python|питон'))

print(works[works.skills.notna()][df]['salary'])