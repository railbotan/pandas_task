import pandas as pd


def non_matches_param_count(firs_param, second_param, df):
    count = 0
    for (f1, f2) in zip(df[firs_param], df[second_param]):
        if not (contains(f1, f2) or contains(f2, f1)):
            count += 1
    return count


def contains(first, second):
    for word in first.lower().replace('-', ' ').split():
        if word in second.lower():
            return True
    return False


def get_top(size, df, searched_f, returned_f, search_s):
    return df[df[searched_f].str.lower().str.contains(search_s[:-2])][returned_f].str.lower().value_counts().head(size)


works = pd.read_csv("works.csv").dropna()
count_not_matches_job = non_matches_param_count("jobTitle", "qualification", works)

print(f"Из {works.shape[0]} людей не совпадают профессия и должность у {count_not_matches_job}")

print("\nЛюди с каким образованием становятся менеджерами (топ-5)?")
print(get_top(5, works, "jobTitle", "qualification", "менеджер"))

print("\nКем работают люди, которые по диплому являются инженерами (топ-5)?")
print(get_top(5, works, "qualification", "jobTitle", "инженер"))
