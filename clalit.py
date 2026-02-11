import pandas as pd
import numpy as np
import os

def load_data(file_path):  
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    try:
        #Reads a CSV file
        df = pd.read_csv(file_path)
        
        if df.empty:
            print("Warning: The loaded file is empty.")
            return df

        print(f"Successfully loaded data from {file_path}")
        
        return df

    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        raise


def stats_for_test(df, lab_codes):
    if isinstance(lab_codes, (int, str)):
        lab_codes = [lab_codes]
        
    all_results = {}
    for code in lab_codes:
        filtered = df[df["lab_code"] == code]["value"]
        if filtered.empty:
            all_results[code] = {"min": None, "max": None, "avg": None}
        else:
            all_results[code] = {
                "min": filtered.min(),
                "max": filtered.max(),
                "avg": filtered.mean()
            }
    
    return all_results

def get_test_stats_from_file(file_obj, lab_codes):
    try:
        df = pd.read_csv(file_obj)
        return stats_for_test(df, lab_codes)
    except Exception as e:
        print(f"Error: {e}")
        return {}



if __name__ == "__main__":
    df = load_data("lab_tests.csv")
    

    print("\nStats for Code 117:")
    stats117 = stats_for_test(df, 117)
    for code, s in stats117.items():
        print(f"Code {code}: Min={s['min']}, Max={s['max']}, Avg={s['avg']}")

    print("\nStats for List [21400, 122] from file:")
    with open("lab_tests.csv", "r") as f:
        multi_stats = get_test_stats_from_file(f, [21400, 122])
        for code, s in multi_stats.items():
            print(f"Code {code}: Min={s['min']}, Max={s['max']}, Avg={s['avg']}")

top_20_tests = (
    df["lab_code"]
    .value_counts()
    .head(20)
    .index
    .tolist()
)

print("\nTop 20 Tests:")
for code in top_20_tests:
    print(f"Code {code}")

wide_df = df[df["lab_code"].isin(top_20_tests)] \
    .pivot_table(
        index="guid_tz",
        columns="lab_code",
        values="value",
        aggfunc="mean"
    )

wide_df.to_csv("lab_results_wide.csv")


from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "שלום עולם"}

print(f"Starting server... : {app}")
