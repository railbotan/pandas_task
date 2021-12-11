import pandas as pd


def count_not_match_people(f1, f2, info):
    count = 0
    for (f1, f2) in zip(info[f1], info[f2]):
        if not find_match_people(f1, f2) and not find_match_people(f2, f1):
            count += 1
    return count


def find_match_people(f1, f2):
    arr = f1.lower().replace('-', ' ').split()
    for word in arr:
        if word in f2.lower():
            return True
    return False


def get_topic(size_t, info, f_search, f_back, str_search):
    return info[info[f_search].str.lower().str.contains(str_search[:-2])][f_back].str.lower(
        ).value_counts().head(size_t)


works = pd.read_csv("works.csv").dropna()
count_not_match_people = count_not_match_people("jobTitle", "qualification", works)
print(f"Из {works.shape[0]} людей не совпадают профессия и должность у {count_not_match_people}")

print("\nОбразование людей, которые работают менеджерами:")
print(get_topic(5, works, "jobTitle", "qualification", "менеджер"))

print("\nДолжности людей, которые имеют диплом инженера:")
print(get_topic(5, works, "qualification", "jobTitle", "инженер"))
