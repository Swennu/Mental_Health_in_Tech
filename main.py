import Data_cleaning
import pandas as pd

if __name__ == "__main__":
    df = Data_cleaning.clean_data()
    Data_cleaning.save_data(df)
    df = df.dropna(subset=['seek_help'])
    X = df.drop('seek_help', axis=1)
    Y = df['seek_help']

    X = pd.get_dummies(X, drop_first=True)
    print("Final shape of features after encoding:", X.shape)
    print("Target:", Y.shape)
