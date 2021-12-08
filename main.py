import pandas as pd


def count_profession_dont_match_qualification(data_frame):
    count = 0
    for (job, qualification) in zip(data_frame["jobTitle"], data_frame['qualification']):
        if is_sub_text_in_text(job, qualification) or is_sub_text_in_text(qualification, job):
            continue
        count += 1
    return count


def is_sub_text_in_text(sub_text: str, text: str) -> bool:
    words = sub_text.split(' ')
    for word in words:
        if word in text:
            return True
    return False


def get_managers_top_qualification(data_frame):
    managers = data_frame[data_frame["jobTitle"].str.contains("менедж")]
    return managers['qualification'].value_counts().head(5)


def get_engineers_top_job(data_frame):
    engineers = data_frame[data_frame["qualification"].str.contains("инженер")]
    return engineers['jobTitle'].value_counts().head(5)


df = pd.read_csv('works.csv')
df = df.dropna()
df = df.apply(lambda x: x.astype(str).str.lower())

all_count = len(df)
print(f"Всего людей: {all_count}.")
dont_match_count = count_profession_dont_match_qualification(df)
print(f"Из которых у {dont_match_count} профессия и должность не совпадают.")
print(f"Что составляет {dont_match_count / all_count:.0%}.")
print()
print("Топ 5 квалификаций менеджеров:")
print(get_managers_top_qualification(df))
print()
print("Топ 5 должностей инженеров:")
print(get_engineers_top_job(df))
