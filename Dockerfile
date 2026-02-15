# 1. בחירת גרסת Python ספציפית - ניהול גרסאות מושלם
FROM python:3.11-slim

# 2. הגדרת תיקיית עבודה בתוך המכולה
WORKDIR /app

# 3. העתקת קובץ הדרישות והתקנתן
# אנחנו מעתיקים קודם את ה-requirements כדי לנצל את ה-Cache של דוקר
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. העתקת שאר קוד המקור של הפרויקט
COPY . .

# 5. פקודה להרצת האפליקציה (למשל סקריפט ראשי)
CMD ["python", "main.py"]