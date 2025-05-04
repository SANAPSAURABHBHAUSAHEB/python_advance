import pandas as pd
import numpy as np
from numpy.random import randint

# read csv file
df = pd.read_csv('D:\python\day11\data.csv')

# print data
# print(df)

df2 = pd.read_excel('D:\python\day11\prm.xlsx')

# print data
# print(df2)

# print(df2[df2["Progress"] > 0.50])

# df = df.dropna()
# print(df)


arr1 = randint(1, 100, size=5)
# print(arr1)

count = arr1.shape[0]
mean = arr1.mean()
std = arr1.std()
min = arr1.min()
percentile1 = np.percentile(arr1, 25)
percentile2 = np.percentile(arr1, 50)
percentile3 = np.percentile(arr1, 75)
max = arr1.max()

# print("Count: ", count)
# print("Mean: ", mean)
# print("Standard Deviation: ", std)
# print("Minimum: ", min)
# print("Percentile 25: ", percentile1)
# print("Percentile 50: ", percentile2)
# print("Percentile 75: ", percentile3)
# print("Maximum: ", max)

# df = pd.Series(arr1)
# print(df.describe())

df3 = pd.read_csv("D:/python/day11/titanic.csv")
# print(df3.shape)
# print(df3.columns)

# print(df3.describe())
# print(df3.info())
# print(df3.head())

# df6 = df3[(df3["Age"] < 15) & (df3["Sex"] == "female")]
# df6 = df3[(df3["Age"] < 5)]
df6 = df3[(df3["Pclass"] == 1)]
print(df6.shape)
print(df6["Survived"].sum()/df6.shape[0] * 100)
print(df6)

# df3["Ticket"].unique()
# df6["Cabin"] = df3["Cabin"].split(" ")[0]

# Conclusion
# 1. 1st class passengers have higher survival rate
# 2. 3rd class passengers have lower survival rate
# 3. on basis of 1st class priority matters (female over male, childen > 10 years)

