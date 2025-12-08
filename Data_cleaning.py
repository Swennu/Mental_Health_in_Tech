import pandas as pd
import numpy as np


def clean_data():
    # Load data
    df = pd.read_csv('data/survey.csv', na_values=['NA', ''])
    # Drop unnecessary columns
    df = df.drop(columns=['Timestamp', 'comments', 'state'], axis=1)

    # Clean 'Gender' column
    df['Gender'] = df['Gender'].str.strip().str.lower()
    male_terms = [
        'male', 'm', 'man', 'male-ish', 'maile', 'mal',
        'male (cis)', 'cis male',
        'make', 'msle', 'cis man', 'mail', 'malr',
        'guy (-ish) ^_^', 'male leaning androgynous',
        'ostensibly male, unsure what that really means'
        ]
    female_terms = [
        'female', 'f', 'woman', 'femake', 'female (cis)', 'cis female',
        'cis-female/femme', 'female (trans)', 'trans woman', 'trans-female'
        ]
    # Iterating through the terms and replacing them with the correct Term
    for term in male_terms:
        df['Gender'] = df['Gender'].replace(term, "Male")
    for term in female_terms:
        df['Gender'] = df['Gender'].replace(term, "Female")
    # Making the gender column into a binary one
    df['Gender'] = df['Gender'].replace({
        'Male': 1,
        'Female': 0
    })
    iter_list = [1, 0]
    df.loc[~df['Gender'].isin(iter_list), 'Gender'] = np.nan

    # Clean 'Age' column
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df = df[(df['Age'] >= 15) & (df['Age'] <= 120)]
    df['self_employed'] = df['self_employed'].fillna('No')

    # Family History
    df['family_history'] = df['family_history'].fillna(np.nan)

    # Fill missing values in 'work_interfere' with mode
    mod = df['work_interfere'].fillna(df['work_interfere'].mode()[0])
    df['work_interfere'] = mod    # Ordinal Encoding for 'work_interfere'

    work_interfere_map = {
        'Never': 0,
        'Rarely': 1,
        'Sometimes': 2,
        'Often': 3
    }
    df['work_interfere'] = df['work_interfere'].map(work_interfere_map)

    leave_map = {
        "Don't know": 0,
        "Somewhat easy": 1,
        "Somewhat difficult": 2,
        "Very difficult": 3
    }
    df['leave'] = df['leave'].map(leave_map)
    df['leave'] = df['leave'].fillna(df['leave'].mode()[0])

    # Ordinal Encoding for 'no_employees'
    employee_map = {
        '1-5': 0,
        '6-25': 1,
        '26-100': 2,
        '100-500': 3,
        '500-1000': 4,
        'More than 1000': 5
    }
    df['no_employees'] = df['no_employees'].map(employee_map)

    # Binary Encoding for Yes/No columns
    binary_cols = [
        'treatment', 'family_history', 'remote_work', 'tech_company',
        'obs_consequence', 'self_employed'
    ]

    for col in binary_cols:
        df[col] = df[col].replace({'Yes': 1, 'No': 0}).astype('float')

    # Convert "Yes/No/Maybe/Some" style to numeric or NaN
    multi_cols = [
        'mental_health_consequence', 'phys_health_consequence',
        'mental_health_interview', 'mental_vs_physical',
        'seek_help', 'benefits', 'care_options',
        'wellness_program', 'anonymity', 'supervisor', 'coworkers'
    ]

    for col in multi_cols:
        df[col] = df[col].replace({'Yes': 1, 'No': 0})

        # Everything else = NaN (Maybe, Not sure, Some of them)
        df.loc[~df[col].isin([0, 1]), col] = np.nan

    # Fill missing values
    fill_mode_cols = [
        'benefits', 'care_options', 'wellness_program',
        'anonymity', 'supervisor', 'coworkers', "Gender"
    ]

    for col in fill_mode_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    zero_fill = [
        'mental_health_consequence', 'phys_health_consequence',
        'mental_health_interview', 'mental_vs_physical', 'seek_help'
    ]
    for col in zero_fill:
        df[col] = df[col].fillna(0)

    # Remove empty strings
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].replace('', np.nan)

    return df


def save_data(df):
    df.to_csv('data/data_cleaned.csv', index=False)
    print("Data cleaned and saved to 'data/data_cleaned.csv'")
