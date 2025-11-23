import Data_cleaning

if __name__ == "__main__":
    df_cleaned = Data_cleaning.clean_data()
    Data_cleaning.save_data(df_cleaned)
