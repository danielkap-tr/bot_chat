
def count_valid_visits(visits):
    result = {}

    for visit in visits:
        patient_id = visit.get("patient_id")
        visit_date = visit.get("visit_date")

        if visit_date is None:
            continue

        result[patient_id] = result.get(patient_id, 0) + 1

    return result


 # רשימת הביקורים
visits = [
    {"patient_id": 1, "visit_date": "2024-01-10", "clinic": "A"},
    {"patient_id": 2, "visit_date": "2024-01-11", "clinic": "B"},
    {"patient_id": 1, "visit_date": "2024-01-15", "clinic": "A"},
    {"patient_id": 3, "visit_date": None, "clinic": "C"},
]

# קריאה לפונקציה מה-"main"
if __name__ == "__main__":
    counts = count_valid_visits(visits)
    print(counts)


