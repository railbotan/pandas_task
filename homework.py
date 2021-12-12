import pandas as pd

def non_matches(firs_param, second_param, data):
    count = 0
    for (f1, f2) in zip(data[firs_param], data[second_param]):
        if not is_contains(f1, f2) and not is_contains(f2, f1):
            count += 1
    return count


def is_contains(first_field, second_field):
    for word in first_field.lower().replace('-', ' ').split():
        if word in second_field.lower():
            return True
    return False


def get_top(size, data, field1, field2, word_to_search):
    return data[data[field1].str.lower().str.contains(word_to_search[:-2])][field2]\
        .str\
        .lower()\
        .value_counts()\
        .head(size)



works = pd.read_csv("works.csv").dropna()
not_matches_count = non_matches("jobTitle", "qualification", works)
managers = get_top(5, works, "jobTitle", "qualification", "менеджер")
engineers = get_top(5, works, "qualification", "jobTitle", "инженер")
output_string = f"{works.shape[0]} не совпадает {not_matches_count}\n\n" \
                f"Топ 5 образовний менеджеров\n" \
                f"{managers}\n\n" \
                f"Топ 5 должностей инженеров\n" \
                f"{engineers}"

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(output_string)