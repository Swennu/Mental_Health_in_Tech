import pandas as pd
import numpy as np


def clean_data():
    # Load data
    df = pd.read_csv('data/survey.csv', na_values=['NA', ''])
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

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
    nb_terms = [
        'non-binary', 'genderqueer', 'androgyne', 'agender', 'enby', 'fluid',
        'neuter', 'queer/she/they'
    ]

    for term in male_terms:
        df['Gender'] = df['Gender'].replace(term, "Male")
    for term in female_terms:
        df['Gender'] = df['Gender'].replace(term, "Female")
    for term in nb_terms:
        df['Gender'] = df['Gender'].replace(term, "Non-Binary")

    iter_list = ['Male', 'Female', 'Non-Binary']
    df.loc[~df['Gender'].isin(iter_list), 'Gender'] = np.nan

    # Clean 'Age' column
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df = df[(df['Age'] >= 15) & (df['Age'] <= 120)]
    df['self_employed'] = df['self_employed'].fillna('No')

    # States
    df.loc[df['Country'] != 'United States', 'state'] = 'N/A'

    df['state'] = df['state'].fillna('Missing')

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
        'treatment',
        'family_history',
        'remote_work',
        'tech_company',
        'obs_consequence',
        'mental_health_consequence',
        'phys_health_consequence',
        'supervisor',
        'benefits',
        'seek_help',
        'mental_health_interview',
        'mental_vs_physical'
        ]
    for col in binary_cols:
        df[col] = df[col].replace({'Yes': 1, 'No': 0, 'Missing': np.nan})

    # Consolidate missing/uncertain responses
    uncertain_responses = ['Don\'t know', 'Not sure']
    cols_to_clean = [
        'benefits', 'care_options',
        'wellness_program', 'seek_help',
        'anonymity'
          ]

    for col in cols_to_clean:
        df[col] = df[col].replace(uncertain_responses, np.nan)

    # Replace empty strings with NaN in all object type columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].replace('', np.nan)

    return df


def save_data(df):
    df.to_csv('data/data_cleaned.csv', index=False)
    print("Data cleaned and saved to 'data/data_cleaned.csv'")
