import pandas as pd

def get_total_marks_count(df):
    total_marks_count = df['Оценка'].notnull().count()
    return total_marks_count

def get_PI101_group_marks_count(df):
    PI101_group_marks_count = df['Группа'].value_counts()['ПИ101']
    return PI101_group_marks_count

def get_students_ids_count(df):
    students_ids = df.loc[df['Группа'] == 'ПИ101', 'Личный номер студента'].nunique()
    return students_ids

def get_PI101_group_students_ids(df):
    PI101_group_students_ids = df.loc[df['Группа'] == 'ПИ101', 'Личный номер студента'].unique().tolist()
    return PI101_group_students_ids

def get_unique_forms_of_control(df):
    forms_of_control = df['Уровень контроля'].unique()
    return forms_of_control

def get_data_interval(df):
    years = df['Год'].unique().tolist()
    return years

def get_students_ids_count(df):
    students_ids = df.loc[df['Группа'] == 'ПИ101', 'Личный номер студента'].nunique()
    return students_ids

def main():
    df = pd.read_excel('lab_pi_101.xlsx')
    print(df)

    total_marks_count = get_total_marks_count(df)
    PI101_group_marks_count = get_PI101_group_marks_count(df)
    print('В исходном датасете содержалось', total_marks_count, 'оценок, из них', PI101_group_marks_count, 'оценок относятся к группе ПИ101')

    students_ids_count = get_students_ids_count(df)
    PI101_group_students_ids = get_PI101_group_students_ids(df)
    print('В датасете находятся оценки', students_ids_count,'студентов со следующими личными номерами(По ПИ101):', ", ".join(map(str, PI101_group_students_ids)))

    forms_of_control = get_unique_forms_of_control(df)
    print('Используемые формы контроля:', ', '.join(map(str,forms_of_control)))
    
    years = get_data_interval(df)
    years.sort()
    print('Данные представлены по следующим учебным годам:',', '.join(map(str,years)))

main()