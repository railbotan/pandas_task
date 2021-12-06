import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

works = pd.read_csv("./works.csv")

m = works[works['gender'] == 'Мужской']['salary'].values
fm = works[works['gender'] == 'Женский']['salary'].values
#print(m.values)
m_pcs = np.percentile(m, [x / 100.0 for x in range(100)])
print(m_pcs[50])
# ax = plt.subplots()[1]
# ax.plot(m_pcs)
#
# plt.show()
