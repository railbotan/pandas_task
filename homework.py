import pandas as pd
import matplotlib.pyplot as plt


def checkToContains(checkableWord, checkedWord):
    words = checkableWord.lower().replace('-', ' ').split()
    for word in words:
        if word in checkedWord.lower():
            return True
    return False


def count(works, column1, column2):
    result = 0
    for job, qualification in zip(works[column1], works[column2]):
        if not checkToContains(job, qualification) and not checkToContains(qualification, job):
            result += 1
    return result


works = pd.read_csv('works.csv').dropna()
result = count(works, 'jobTitle', 'qualification')

top5_menegers = works[works['jobTitle'].str.lower().str.contains('менеджер'[:-2])]['qualification'].str.lower()
top5_engeners = works[works['jobTitle'].str.lower().str.contains('инженер'[:-2])]['qualification'].str.lower()

plt.bar(top5_menegers.head(5).values, top5_menegers.value_counts().head(5).values, color='blue',
        label='образование у менеджеров')
plt.bar(top5_engeners.head(5).values, top5_engeners.value_counts().head(5).values, color='red',
        label='образование у инженеров')

plt.legend()
plt.show()
