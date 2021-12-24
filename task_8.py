import pandas as pd


def non_matches_fields_count(firs_param, second_param, df):
    count = 0
    for (f1, f2) in zip(df[firs_param], df[second_param]):
        if not is_contains(f1, f2) and not is_contains(f2, f1):
            count += 1
    return count


def is_contains(first_f, second_f2):
    for word in first_f.lower().replace('-', ' ').split():
        if word in second_f2.lower():
            return True
    return False


def get_top(size, df, searched_f, returned_f, search_s):
    return df[df[searched_f].str.lower().str.contains(search_s[:-2])][returned_f].str.lower().value_counts().head(size)


works = pd.read_csv("works.csv").dropna()
count_not_matches_job = non_matches_fields_count("jobTitle", "qualification", works)

print(f"Из {works.shape[0]} людей не совпадают профессия и должность у {count_not_matches_job}")

print("\nТоп - 5 образований менеджеров ")
print(get_top(5, works, "jobTitle", "qualification", "менеджер"))

print("\nТоп - 5 должностей инженеров")
print(get_top(5, works, "qualification", "jobTitle", "инженер"))

