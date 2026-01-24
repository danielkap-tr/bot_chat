visits = [
    {"id": 1, "date": "2024-01-01", "cost": 100},
    {"id": 2, "date": None, "cost": 80},
    {"id": 3, "date": "2024-02-10", "cost": 120},
]


visits_valid = [visit for visit in visits if visit["date"] is not None]
print(visits_valid)



import pandas as pd

df = pd.DataFrame(visits)
print(df)