import pandas as pd


def get_match_count(first_list, second_list):
    return len(list((filter(lambda x: contains(x[0], x[1]) or contains(x[1], x[0]), zip(first_list, second_list)))))


def contains(sub_text, text):
    words = sub_text.replace('-', ' ').split(' ')
    for word in words:
        if word in text:
            return True
    return False


def get_top(source, search_field, return_field, value):
    return source[source[search_field].str.contains(value)][return_field].value_counts().head(5)


data = pd.read_csv('works.csv').dropna().apply(lambda x: x.astype(str).str.lower())
count = len(data)
mismatch_count = count - get_match_count(data["jobTitle"], data["qualification"])

print(f"Всего людей: {count}.")
print(f"Людей с несовпадающими профессией и должностью: {mismatch_count}.")
print(f"Что составляет {mismatch_count / count:.0%} от общего числа.")
print("\nТоп 5 квалификаций менеджеров:")
print(get_top(data, "jobTitle", "qualification", "менеджер"))
print("\nТоп 5 должностей инженеров:")
print(get_top(data, "qualification", "jobTitle", "инженер"))
