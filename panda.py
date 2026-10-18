import pandas as pd

data = {
    "Name": ["Aarav", "Riya", "Kabir", "Ananya"],
    "Hours": [2, 4, 3, 5],
    "Marks": [50, 85, 70, 95]
}

df = pd.DataFrame(data)
df["Marks"]              # One column → Series
df[["Name", "Marks"]]    # Multiple columns → DataFrame

df[df["Marks"] > 70]
df[df["Hours"] >= 3]                  # Hours at least 3
df[df["Marks"] == 70]                 # Marks exactly 70
df[df["Marks"] < 60]                  # Marks below 60



#CLEANING DATA
import numpy as np

data = {
    "Name": ["Aarav", "Riya", "Kabir", "Ananya"],
    "Hours": [2, 4, np.nan, 5],
    "Marks": [50, 85, 70, np.nan]
}

df = pd.DataFrame(data)
print(df)
df.isna()
df.isna().sum()
df.dropna()  # Drop rows with NaN values
df["Hours"] = df["Hours"].fillna(df["Hours"].mean()) # Fill NaN values in Hours column with the mean
df["Marks"] = df["Marks"].fillna(df["Marks"].median()) # Fill NaN values in Marks column with the median


data={
    "name":{["riddhi","kanha","laddoo"],
            "hours":{[2,3,4]},
            "marks":{[90,98,89]}}
}
df= pd.DataFrames(data)

import pandas as pd

data = {
    "Name": ["Aarav", "Riya", "Kabir", "Ananya", "Dev"],
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE"],
    "Hours": [2, 4, 3, 5, 1],
    "Marks": [50, 85, 70, 95, 40]
}

df = pd.DataFrame(data)

df.sort_values("Marks",ascending=False)  # Sort by Marks in descending order
df.sort_values("Hours")
#pandas can help us to calculate stats
df["Marks"].mean()    # Average marks
df["Marks"].max()     # Highest marks
df["Marks"].min()     # Lowest marks
df["Marks"].median()  # Middle value
df["Marks"].sum()     # Total marks

df.describe()  # Summary statistics for numerical columns
df.groupby("Department")["Marks"].mean()  # Average marks by department

df.duplicated()  # Check for duplicate rows
df.drop_duplicates()  # Remove duplicate rows
df.duplicated(subset=["Name"])
df[(df["Department"]=="CSE")& (df["Marks"]>60)]  # CSE students with marks greater than 60


#loading a real dataset from csv file

df=pd.read_csv("students.csv")  # Load data from a CSV file
df.head()          # First 5 rows
df.tail()          # Last 5 rows
df.shape           # Number of rows and columns
df.columns         # Column names
df.info()          # Column types and non-missing counts
df.isna().sum()    # Missing-value counts
df.describe()     # Numerical summary
