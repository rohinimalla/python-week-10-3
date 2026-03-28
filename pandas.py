import pandas as pd
import numpy as np
data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [85, None, 78, 90],
    "Age": [20, 21, None, 22]
}
df = pd.DataFrame(data)
print("Original Data:\n", df)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Grade"] = ["B", "A", "C", "A"]
df.rename(columns={"Marks": "Score"}, inplace=True)
df.drop("Grade", axis=1, inplace=True)
df.drop_duplicates(inplace=True)
print("\nCleaned Data:\n", df)
