import pandas as pd


def incongruity_count(f, s, t):
    count = 0
    for (f1, f2) in zip(t[f], t[s]):
        if isnt_contains(f1, f2) and isnt_contains(f2, f1):
            count += 1
    return count


def isnt_contains(f, s):
    for word in f.lower().replace('-', ' ').split():
        if word not in s.lower():
            return True
    return False


def get_top(s, t, a, b, w):
    return t[t[a].str.lower().str.contains(w[:-2])][b].str.lower().value_counts().head(s)


works = pd.read_csv("../works.csv").dropna()

inconsistencies = incongruity_count("jobTitle", "qualification", works)
managers = get_top(5, works, "jobTitle", "qualification", "менеджер")
engineers = get_top(5, works, "qualification", "jobTitle", "инженер")
print(f"Всего записей {works.shape[0]}. Из них не совпадают {inconsistencies}\n\n"
      f"Топ - 5 образований менеджеров\n"
      f"{managers}\n\n"
      f"Топ - 5 должностей инженеров\n"
      f"{engineers}")
