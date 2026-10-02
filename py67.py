import pandas as pd


marks = pd.Series(
    [75, 82, 68, 90, 55],
    index=["Shiva", "Mika", "Vashnavi", "Amelia", "Joshua"]
)

print("Student Marks:")
print(marks)


data = {
    "Name": ["Shiva", "Mika", "Vashnavi", "Amelia", "Joshua"],
    "Math": [75, 82, 68, 90, 55],
    "English": [80, 78, 72, 85, 60],
    "Science": [70, 88, 75, 92, 65]
}

df = pd.DataFrame(data)

print("\nStudent Data:")
print(df)


df.to_csv("student_marks.csv", index=False)


df = pd.read_csv("student_marks.csv")

print("\nCSV Data:")
print(df)

print("\nFirst 5 Rows:")
print(df.head())


print("\nData Information:")
print(df.info())


print("\nMissing Values:")
print(df.isnull().sum())


df = df.fillna(0)

df["Total"] = df["Math"] + df["English"] + df["Science"]

df["Average"] = df["Total"] / 3

print("\nFinal Student Marks:")
print(df)
