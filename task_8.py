import pandas as pd


def no_match_counter(firs_param, second_param, elements):
    count = 0

    for (f1, f2) in zip(elements[firs_param], elements[second_param]):
        if not (contains(f1, f2) or contains(f2, f1)):
            count += 1

    return count


def contains(first, second):

    for word in first.lower().replace('-', ' ').split():
        if word in second.lower():
            return True

    return False


def get_job_list(size, df, searched_f, returned_f, search_s):
    return df[df[searched_f].str.lower().str.contains(search_s[:-2])][returned_f].str.lower().value_counts().head(size)


data = pd.read_csv("works.csv").dropna()
count_not_matches_job = no_match_counter("jobTitle", "qualification", data)

print(f"Из {data.shape[0]} людей не совпадают профессия и должность у {count_not_matches_job}")

print("\nЛюди с таким образованием становятся менеджерами: ")
print(get_job_list(5, data, "jobTitle", "qualification", "менеджер"))

print("\nКем работают люди имеющие диплом инженера: ")
print(get_job_list(5, data, "qualification", "jobTitle", "инженер"))