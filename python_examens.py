data = [
    {"patient_id": 1, "visit_date": "2024-01-01"},
    {"patient_id": 2, "visit_date": "2024-02-01"},
    {"patient_id": 1, "visit_date": "2024-02-01"},
    {"patient_id": 3, "visit_date": None}
]


def count_valid_visits(data):
    counts = {}
    for item in data:
        patient_id = item.get("patient_id")
        visit_date = item.get("visit_date")
        if visit_date is not None:
            counts[patient_id] = counts.get(patient_id, 0) + 1
    return counts


from collections import defaultdict

def count_valid_visits_2(data):
    counts = defaultdict(int)
    for item in data:
        if item.get("visit_date") is not None:
            counts[item["patient_id"]] += 1
    return dict(counts)






if __name__ == "__main__":
    counts = count_valid_visits(data)
    print(counts)

    counts = count_valid_visits_2(data)
    print(counts)

    import pandas as pd

    df_visits = pd.DataFrame({
        "patient_id": [1, 2, 1, 3, 2, 4],
        "visit_date": [
            "2024-01-01",
            "2024-01-05",
            "2024-02-01",
            "2024-01-10",
            "2024-02-20",
            None
        ]
    })

    print(df_visits)


    result = (
        df_visits
        .groupby("patient_id")
        .size()
        .reset_index(name="visit_count")
        .query("visit_count > 1")
    )

    print(result)

    df_visits = df_visits.dropna(subset=["visit_date"])
    print("df_visits after dropping null values:")
    print(df_visits)

    visit_counts = df_visits.groupby("patient_id").size().reset_index(name="visit_count")
    result = visit_counts[visit_counts["visit_count"] > 1]

    print(result)

# ALTER TABLE visits
# ADD CONSTRAINT uq_patient_visit
# UNIQUE (patient_id, visit_date);


#     def insert_visit(cursor, patient_id, visit_date):
#     query = """
#     INSERT INTO visits (patient_id, visit_date)
#     VALUES (%s, %s)
#     ON CONFLICT (patient_id, visit_date) DO NOTHING
#     """
#     cursor.execute(query, (patient_id, visit_date))
