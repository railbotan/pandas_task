import pandas as pd


def count_not_match_fields(field1, field2, data):
    res_count = 0
    for (f1, f2) in zip(data[field1], data[field2]):
        if not is_match(f1, f2) and not is_match(f2, f1):
            res_count += 1
    return res_count


def get_top(size, data, searched, returned, search_str):
    return data[data[searched].str.lower().str.contains(search_str[:-2])][returned].str.lower().value_counts().head(size)


def is_match(field1, field2):
    for word in field1.lower().replace('-', ' ').split():
        if word in field2.lower():
            return True
    return False


works = pd.read_csv("works.csv").dropna()
count_not_match = count_not_match_fields("jobTitle", "qualification", works)
print(f"Из {works.shape[0]} людей не совпадают профессия и должность у {count_not_match}")

print("\nТоп образований людей, которые работают менеджерами")
print(get_top(5, works, "jobTitle", "qualification", "менеджер"))

print("\nТоп должностей людей, которые по диплому являются инженерами")
print(get_top(5, works, "qualification", "jobTitle", "инженер"))
