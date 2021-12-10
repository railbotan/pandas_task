import pandas as pd

def find_profession_and_position(file):
    answer = 0
    for (j, q) in zip(file["jobTitle"], file["qualification"]):
        if not find(j, q) and not find(q, j):
            answer += 1
    return answer

def find(one, two):
    m = one.lower().replace('-', ' ').split()
    for e in m:
        if e in two.lower():
            return True
    return False

works = pd.read_csv('works.csv').dropna()

print('1. Профессия и должность не совпадают у {} человек.'.format(find_profession_and_position(works)))

print('2. Топ-5 образований, с которыми люди становятся менеджерами:')
print(works[works["jobTitle"].str.lower()
    .str.contains("менеджер")]["qualification"].str.lower().value_counts().head(5))

print('3. Топ-5 профессий людей, получивших диплом инженера:')
print(works[works["qualification"].str.lower()
    .str.contains("инженер")]["jobTitle"].str.lower().value_counts().head(5))