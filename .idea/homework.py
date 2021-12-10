import pandas as pd

def upper(upper_size, info, field_search, field_return, str_search):
    return info[info[field_search].str.lower().str.contains(
        str_search[:-2])][field_return].str.lower().value_counts().head(upper_size)

def number_people_whose_profession_did_not_match(field_1, field_2, info):
    result_count = 0
    for (f_1, f_2) in zip(info[field_1], info[field_2]):
        if not look_match_people_and_profession(f_1, f_2) and not look_match_people_and_profession(f_2, f_1):
            result_count += 1
    return result_count

def look_match_people_and_profession(f_1, f_2):
    arr_1 = f_1.lower().replace('-', ' ').split()
    for word in arr_1:
        if word in f_2.lower():
            return True
    return False

works = pd.read_csv("works.csv").dropna()
count_prof_not_match_qualif = number_people_whose_profession_did_not_match("jobTitle", "qualification", works)
print("Из {} людей не совпадение по профессии и должности имеют {} человека".format(works.shape[0], count_prof_not_match_qualif))

print("\nСамые популярные образования людей, которые работают менеджерами")
print(upper(5, works, "jobTitle", "qualification", "менеджер"))

print("\nЛюди, которые по диплому являются инженерами, имеют такие популярные должности, как:")
print(upper(5, works, "qualification", "jobTitle", "инженер"))