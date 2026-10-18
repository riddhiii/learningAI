import pandas as pd
import numpy as np

data = {
    "Name": ["Aarav", "Riya", "Kabir", "Ananya", "Dev", "Riya"],
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE", "ECE"],
    "Hours": [2, 4, 3, 5, 1, 4],
    "Marks": [50, 85, 70, 95, 40, 85]
}

df = pd.DataFrame(data)

print(df.head())
print(df.shape)
print(df.columns)
print(df["Marks"].mean()) 

print(df[(df["Hours"]>=30) & (df["Marks"]>=70)])
print(df.groupby("Department")["Marks"].mean())  # Average marks by department
print(df.duplicated())  # Check for duplicate rows



