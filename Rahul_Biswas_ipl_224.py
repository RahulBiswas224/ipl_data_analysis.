import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 


data = pd.read_csv("ipl.csv")
df = pd.DataFrame(data)


# data analysis
print("\n printing all data")
print(df)

print("\nshowing shape of data ")
print(df.shape)

print("\nshowing columns ")
print(df.columns)

print("\nshowing columns val")
print(df.columns.values)

print("\nshowing describe")
print(df.describe)

print("\nshowing info ")
print(df.info())

print("\ndata form top 10 row ")
print(df.head(10))

print("\ndata form tail 10 row ")
print(df.tail(10))

print("\nmax win_by_runs ")
print(df["win_by_runs"].max())

print("\nmin win_by_runs ")
print(df["win_by_runs"].min())

print("\nshowing data whosewin_by_runs greater than 30")
print(df[df.win_by_runs>30])

print("\nshowing data from row 2 to 5")
print(df[2:6])


#missing value finding 

print("printing null values columns in dataframe ")
print(df.isnull())

print("finding missing value of win_by_runs column")
print(df[df["win_by_runs"].isnull()])

print("finding missing value of umpire3 column")
print(df[df["umpire3"].isnull()])


# matplot lib plotting 


plt.plot(df["win_by_runs"],df["win_by_wickets"])

plt.scatter(df["win_by_runs"],df["win_by_wickets"])

plt.boxplot(df["win_by_runs"])


# seaborn plotting 

sns.barplot(x = "result", y = "toss_winner",data = df, hue="win_by_runs")

sns.jointplot(x = "result", y = "toss_winner",data = df) 

sns.pairplot(df,hue="result",palette="Reds") 

sns.boxplot(x="result" , y= "toss_winner",data= df)

sns.scatterplot(x="result",y="toss_winner",hue="win_by_runs" , data=df)

sns.histplot(df["result"],kde=False,bins=20)

plt.show()
