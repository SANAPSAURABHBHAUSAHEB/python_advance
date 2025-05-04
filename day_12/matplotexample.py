import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import seaborn as sns
# sns.set_theme(style="ticks")

# df = sns.load_dataset("penguins")
# sns.pairplot(df, hue="species")
# plt.show()

# ename = ["rijual","namoh","vipul"]
# salary =[99000,90000,80000,]
# plt.scatter(ename,salary)
# plt.show()


# df1 = pd.read_csv("C:/Users/DAI.STUDENTSDC/Downloads/data1.csv")
# plt.bar(df1["emp_name"],df1["emp_salary"],color=["purple","black"])
# plt.show()
# how to change scalenumpn
# plotnum=np.random.randint(1,100,size = (100,10))
# dfnum = pd.DataFrame(plotnum)
# plt.bar(dfnum[0],dfnum[1])     

# plt.show()

df = pd.read_csv("D:/python/day11/titanic.csv")
# print(df.describe())
# plt.subplot(2,2,1)
# plt.scatter(df["Fare"], df["Age"])
# plt.subplot(2,2,2)
# plt.bar(df["Fare"], df["Age"])
# plt.grid(axis="y")
##subplots

# plt.subplot(2,2,3)
# plt.bar(df["Survived"], df["Age"])
# plt.subplot(2,2,4)
# plt.bar(df["Survived"], df["Fare"])
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# from matplotlib import cm

# plt.style.use('_mpl-gallery')

# # Make data
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)

# # Plot the surface
# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)

# ax.set(xticklabels=[],
#        yticklabels=[],
#        zticklabels=[])

# plt.show()


plt.hist(df["Pclass"])
plt.show()