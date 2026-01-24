import pandas as pd
import numpy as np
import os

def load_and_clean_data(file_path):
    """
    Reads a CSV file, cleans the data, and returns a pandas DataFrame.
    
    Cleaning steps:
    1. Strip whitespace from string columns.
    2. Drop rows with all missing values.
    3. Fill or drop specific missing values (configurable).
    4. Remove duplicate rows.
    5. Attempt to parse date columns.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    try:
        # Load the CSV
        df = pd.read_csv(file_path)
        
        if df.empty:
            print("Warning: The loaded file is empty.")
            return df

        # 0. Strip whitespace from column names
        df.columns = df.columns.str.strip()

        # 1. Strip whitespace from string columns
        df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

        # 2. Drop rows where all elements are missing
        df = df.dropna(how='all')

        # 3. Remove duplicates
        df = df.drop_duplicates()

        # 4. Attempt to convert columns to datetime if they look like dates
        for col in df.columns:
            if 'date' in col.lower() or 'time' in col.lower():
                # Use errors='coerce' to turn invalid dates into NaT
                df[col] = pd.to_datetime(df[col], errors='coerce')

        print(f"Successfully loaded and cleaned data from {file_path}")
        print(f"Shape: {df.shape}")
        
        return df

    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        raise

if __name__ == "__main__":
    # Example usage (will fail if sample.csv doesn't exist yet)
    # df = load_and_clean_data("sample.csv")
    pass
