import pandas as pd

# Simulated data
data = {
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
    'Age': [16, 17, 16, 18, 17],
    'StudyHours': [5, 8, 2, 6, 9],
    'Attendance': [90, 95, 60, 85, 98],
    'ParentalEducation': ['High School', 'Bachelor', 'High School', 'Master', 'Bachelor'],
    'Passed': [1, 1, 0, 1, 1]  # 1 = Passed, 0 = Failed
}

df = pd.DataFrame(data)
print(df)
