import pandas as pd


works = pd.read_csv('works.csv').dropna()


def count(f1, f2, works):
    result = 0
    for n1, n2 in zip(works[f1], works[f2]):
        if not match(n1, n2) and not match(n2, n1):
            result += 1
    return result


def match(c1, c2):
    array = c1.lower().replace('-', ' ').split()
    for word in array:
        if word in c2.lower():
            return True
    return False


result = count('jobTitle', 'qualification', works)
print('Из {} людей не совпадают профессия и должность у {}'.format(works.shape[0], result))

print('\nТоп образований для менеджеров:')
print(
    works[works['jobTitle'].str.lower().str.contains('менеджер'[:-2])]['qualification'].str.lower().value_counts().head(
        5))

print('\nТоп образований для инженеров:')
print(
    works[works['jobTitle'].str.lower().str.contains('инженер'[:-2])]['qualification'].str.lower().value_counts().head(
        5))