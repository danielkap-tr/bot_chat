from data_loader import load_and_clean_data
import pandas as pd

def test_loader():
    file_path = "sample_data.csv"
    
    print("Testing load_and_clean_data...")
    df = load_and_clean_data(file_path)
    
    print("\nCleaned DataFrame:")
    print(df)
    print("\nColumn Types:")
    print(df.dtypes)
    
    # Assertions
    # 1. No empty rows (the ,,, row should be gone)
    assert len(df) == 4, f"Expected 4 rows, got {len(df)}"
    
    # 2. No duplicates
    assert df['id'].is_unique, "Duplicates were not removed"
    
    # 3. Strings are stripped
    assert df.iloc[0]['name'] == 'Alice', f"String not stripped: '{df.iloc[0]['name']}'"
    assert df.iloc[2]['name'] == 'Charlie', f"String not stripped: '{df.iloc[2]['name']}'"
    
    # 4. Date column converted
    assert pd.api.types.is_datetime64_any_dtype(df['date_joined']), "Date column not converted"
    
    print("\nAll tests passed!")

if __name__ == "__main__":
    test_loader()
