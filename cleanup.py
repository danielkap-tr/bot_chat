import os
import shutil

def clean_temp_folders():
    # רשימת התיקיות לניקוי
    folders_to_clean = [
        os.environ.get('TEMP'),                       # %temp% המשתמש
        r'C:\Windows\Temp',                           # temp המערכת
        os.path.expanduser('~\\AppData\\Local\\Microsoft\\Power BI Desktop\\User Data\\Temp') # מטמון פאוור בי
    ]

    print("--- Starting Cleanup Process ---")
    
    for folder in folders_to_clean:
        if folder and os.path.exists(folder):
            print(f"Cleaning: {folder}")
            # מעבר על כל הקבצים והתיקיות בתוך התיקייה
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path) # מחיקת קובץ
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path) # מחיקת תיקייה
                except Exception as e:
                    # קבצים שבשימוש כרגע לא יימחקו וזה תקין
                    pass 
    
    print("--- Cleanup Finished Successfully ---")

if __name__ == "__main__":
    clean_temp_folders()