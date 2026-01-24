visits = [
    {"patient_id": 1, "visit_date": "2024-01-01", "cost": 120},
    {"patient_id": 1, "visit_date": None, "cost": 80},
    {"patient_id": 2, "visit_date": "2024-02-10", "cost": 200},
    {"patient_id": 2, "visit_date": "2024-03-01", "cost": 150},
]


def count_visits(visits):
    count = {}
    for visit in visits:
        v_patient_id = visit.get("patient_id")
        v_visit_date = visit.get("visit_date")     
        v_cost = visit.get("cost")
        if v_visit_date is not None:
            if v_patient_id in count:
                count[v_patient_id] += v_cost
            else:
                count[v_patient_id] = v_cost
    return count


print(count_visits(visits))


# כתוב פונקציה שמחזירה מילון:

# מפתח: patient_id

# ערך: סך עלות הביקורים התקפים בלבד (עם תאריך)


