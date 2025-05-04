import pandas as pd
import numpy as np

df = pd.read_csv("D:/python/day11/titanic.csv")

print(df.describe())

# Differences between NumPy and pandas:
# 1. NumPy is mainly used for numerical computations on arrays, while pandas is used for data manipulation and analysis.
# 2. NumPy provides support for multi-dimensional arrays, whereas pandas provides data structures like Series and DataFrame.
# 3. pandas has built-in support for handling missing data, while NumPy requires manual handling.
# 4. pandas is more suited for working with labeled data, while NumPy works with numerical data without labels.
# 5. pandas offers high-level operations like groupby, merging, and reshaping, which are not available in NumPy.

# count = df.shape[0]
# mean = arr1.mean()
# std = arr1.std()
# min = arr1.min()
# percentile1 = np.percentile(arr1, 25)
# percentile2 = np.percentile(arr1, 50)
# percentile3 = np.percentile(arr1, 75)
# max = arr1.max()
print(df.Survived.mean())
print(df.Age.mean())
print(df.Fare.mean())
print(df.Pclass.mean())
print(df.Survived.std())
print(df.Age.std())
print(df.aggregate({"Survived":  ["mean", "std", "min", "max", "count"]}))
print(df.aggregate({"Age":["m","std","max","count"]}))