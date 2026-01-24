#python_df_join
import pandas as pd

# טבלת מטופלים
patients = pd.DataFrame([
    {"patient_id": 1, "age": 30},
    {"patient_id": 2, "age": 45},
    {"patient_id": 3, "age": 70},
])

# טבלת ביקורים
visits = pd.DataFrame([
    {"patient_id": 1, "clinic": "A", "cost": 100},
    {"patient_id": 1, "clinic": "A", "cost": 150},
    {"patient_id": 2, "clinic": "B", "cost": 200},
    {"patient_id": 3, "clinic": "A", "cost": 120},
])

merged_df = pd.merge(visits, patients, on="patient_id", how="inner")
print(merged_df)
