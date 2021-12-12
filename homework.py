import pandas as pd


def does_not_match(jobTitle, qualification, data):
    count = 0
    for (first_field, second_field) in zip(data[jobTitle], data[qualification]):
        if not it_coincided(first_field, second_field) and not it_coincided(second_field, first_field):
            count += 1
    return count


def it_coincided(first_field, second_field):
    words = first_field.lower().replace('-', ' ').split()
    for word in words:
        if word in second_field.lower():
            return True
    return False


def top_people(top_number, data, first_field, second_field, search_word):
    return data[data[first_field].str.lower().str.contains(search_word[:-2])][second_field].str.lower().value_counts() \
        .head(top_number)


works = pd.read_csv("works.csv").dropna()

does_not_match_count = does_not_match("jobTitle", "qualification", works)
print(f"Из {works.shape[0]} людей должность и профессия не совпадают у {does_not_match_count}.\n")

print("Топ-5 образований людей, которые работают менеджерами:")
print(top_people(5, works, "jobTitle", "qualification", "менеджер"), "\n")

print("Топ-5 должностей людей, которые по диплому являются инженерами")
print(top_people(5, works, "qualification", "jobTitle", "инженер"), "\n")
