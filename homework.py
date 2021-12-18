import pandas as pd

data = pd.read_csv('works.csv')
data

data.dropna(subset=['jobTitle'], inplace=True)
data.dropna(subset=['qualification'], inplace=True)

data.shape[0]

data['qualification'] = data['qualification'].str.replace('-', ' ')
data["jobTitle"] = data["jobTitle"].str.replace('-', ' ')

# Профессия и должность не совпадают
(data['jobTitle'] == data['qualification']).value_counts()

def comparison(column1, column2):
    list1 = column1.split()
    for word in list1:
        if word in column2:
            return True
    return False

count = 0
for (job, qualification) in zip(data["jobTitle"], data["qualification"]):
    if comparison(job, qualification) or comparison(qualification, job):
        count += 1

data.shape[0] - count

# Топ-5 образовний менеджеров
managers = data[data["jobTitle"].str.lower().str.contains("менедж")]
managers['qualification'].str.lower().value_counts().head(5)

# Топ-5 образовний инженеров
engineers = data[data["qualification"].str.lower().str.contains("инженер")]
engineers['jobTitle'].str.lower().value_counts().head(5)