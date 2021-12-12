import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

works = pd.read_csv("works.csv")

#1
print(works.shape[0])

#2
print(works[works['gender'] == 'Мужской'].shape[0], works[works['gender'] == 'Женский'].shape[0])

#3
print(works['skills'].notna().values.sum())

#4
print(works[works['skills'].notna()])
#print(works.query("skills == skills")["skills"])

#5
df = works.skills.dropna().str.lower().str.contains('python|питон')
print(works[works.skills.notna()][df]['salary'])

#6
percentiles = np.linspace(.1, 1, 10)

men_salary = works.query('gender == "Мужской"').quantile(percentiles)
women_salary = works.query('gender == "Женский"').quantile(percentiles)

fig, ax = plt.subplots()
ax.plot(percentiles, men_salary)
plt.xlabel("Перцентили")
plt.ylabel("Зарплата мужчин")

plt.show()

fig, ax = plt.subplots()
ax.plot(percentiles, men_salary)
plt.xlabel("Перцентили")
plt.ylabel("Зарплата женщин")

plt.show()

#7
works.query("gender == 'Мужской' and educationType == 'Высшее'").hist(bins=100, alpha=0.5)
plt.show()

works.query("gender == 'Женский' and educationType == 'Высшее'").hist(bins=100, alpha=0.5)
plt.show()

#8
def count_people_diploma_not_match_job(data):
    result = 0
    for (jt, q) in zip(data["jobTitle"], data["qualification"]):
        if not does_diploma_match(jt, q) and not does_diploma_match(q, jt):
            result += 1
    return result

def get_top_job(data, job, first_parameter, second_parameter):
    workers = data[data[first_parameter].str.contains(job)]
    return workers[second_parameter].value_counts().head(5)

def does_diploma_match(str1, str2):
    str_array = str1.lower().replace('-', ' ').split()
    for word in str_array:
        if word in str2.lower():
            return True
    return False

works = pd.read_csv("works.csv").dropna()
works = works.apply(lambda record: record.astype(str).str.lower())
number_of_people = count_people_diploma_not_match_job(works)
print("Из {} людей не совпадают профессия и должность у {}".format(works.shape[0], number_of_people))

print("\nТоп образований людей, которые работают менеджерами:")
print(get_top_job(works, "менеджер", "jobTitle", "qualification"))

print("\nТоп должностей людей, которые по диплому являются инженерами:")
print(get_top_job(works, "инженер", "qualification", "jobTitle"))