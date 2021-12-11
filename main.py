import numpy as np
import pandas as pd


def calculate_mismatches_between_profession_and_qualification(data):
    result = 0
    for (job, qualification) in zip(data["jobTitle"], data['qualification']):
        if not check_substring(job, qualification) and not check_substring(qualification, job):
            result += 1
    return result


def check_substring(substring, string) -> bool:
    words = substring.split(' ')
    for word in words:
        if word in string:
            return True

    return False


def get_profession_top_by_parameter(data, profession, first_parameter, second_parameter):
    workers = data[data[first_parameter].str.contains(profession)]
    return workers[second_parameter].value_counts().head(5)


works = pd.read_csv('works.csv').dropna()
works_lower = works.apply(lambda record: record.astype(str).str.lower())

count_mismatches = calculate_mismatches_between_profession_and_qualification(works_lower)
print(count_mismatches)
print(works.shape[0])

managers_top = get_profession_top_by_parameter(works_lower, "менеджер", "jobTitle", "qualification")
print(managers_top)
engineers_top = get_profession_top_by_parameter(works_lower, "инженер", "qualification", "jobTitle")
print(engineers_top)
