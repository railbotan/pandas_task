import pandas

works = pandas.read_csv("works.csv").dropna()


def count(field1, field2, jobs):
    res = 0
    for f1, f2 in zip(jobs[field1], jobs[field2]):
        if not comp(f1, f2) and not comp(f2, f1):
            res += 1
    return res


def comp(f1, f2):
    array = f1.lower().replace('-', ' ').split()
    for word in array:
        if word in f2.lower():
            return True
    return False


result = count("jobTitle", "qualification", works)
print("Из {} людей не совпадают профессия и должность у {}".format(works.shape[0], result))

print("\nТоп образований людей для менеджеров")
print(
    works[works['jobTitle'].str.lower().str.contains('менеджер'[:-2])]['qualification'].str.lower().value_counts().head(
        5))

print("\nТоп должностей людей, которые по диплому являются инженерами")
print(
    works[works['jobTitle'].str.lower().str.contains('инженер'[:-2])]['qualification'].str.lower().value_counts().head(
        5))
