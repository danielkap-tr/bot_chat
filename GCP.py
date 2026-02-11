from google.cloud import bigquery
import os

# 1. הזדהות (כמו מקודם)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "mythical-legend-458720-d4-f2b14189d545.json"

def upload_csv_to_bigquery():
    client = bigquery.Client()

    # הגדרת ה-Dataset
    dataset_id = "mythical-legend-458720-d4.customer_dataset"
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "EU" # אפשר לשנות מיקום לפי הצורך (למשל 'EU')
    
    # יצירת ה-Dataset אם הוא לא קיים
    client.create_dataset(dataset, exists_ok=True)
    print(f"Ensured dataset {dataset_id} exists.")

    table_id = f"{dataset_id}.customers_table_2"

    # הגדרות הטעינה (Job Configuration)
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV, # סוג הקובץ
        skip_leading_rows=1,                     # דילוג על שורת הכותרת
        
        autodetect=True,                         # זיהוי אוטומטי של סוגי עמודות (Schema)
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND # הוספה לקיים (אפשר גם WRITE_TRUNCATE לדריסה)
    )

    file_path = "customers.csv"

    # פתיחת הקובץ וטעינה
    with open(file_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)

    print("Starting upload job...")
    
    # המתנה לסיום התהליך (זה קורה ברקע, הפקודה הזו מחכה לתשובה סופית)
    job.result()  

    # בדיקה כמה שורות נטענו
    table = client.get_table(table_id)
    print(f"Loaded {table.num_rows} rows to table {table_id}")

if __name__ == "__main__":
    upload_csv_to_bigquery()